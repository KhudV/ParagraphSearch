# -*- coding: utf-8 -*-
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from interface import SearchRequest, ProcessedSearchRequest
from interface import IndexRequest, ProcessedIndexRequest


# Загрузка модели и токенизатора
model = AutoModel.from_pretrained("./models/multilingual-e5-base")
tokenizer = AutoTokenizer.from_pretrained("./models/multilingual-e5-base")


# Функция для генерации эмбеддингов
def generate_embeddings(text: str, model: torch.nn.Module, tokenizer: AutoTokenizer) -> np.ndarray:
    """
    Генерирует эмбеддинги для заданного текста с использованием указанной модели и токенизатора.

    Параметры:
    ----------
    text : str
        Входной текст, для которого необходимо сгенерировать эмбеддинги.
    
    model : torch.nn.Module
        Модель, использующаяся для генерации эмбеддингов. Ожидается, что модель возвращает
        выходные данные, содержащие скрытые состояния.

    tokenizer : AutoTokenizer
        Токенизатор, используемый для преобразования текста в формат, подходящий для модели.

    Возвращает:
    ----------
    np.ndarray
        Эмбеддинг текста, представленное как массив NumPy.
        Размерность: (размерность векторов эмбеддингов,).
    """
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embeddings


# Функция для преобразования объектов от запроса на поиск
def processIndex(request: IndexRequest) -> ProcessedIndexRequest:

    queries = '' if request.queries is None else ' '.join(request.queries)
    keywords = ''
    for keyword in request.keywords_or_phrases:
        if keyword['keyword_or_phrase'] is not None and \
                                keyword['explanation'] is not None:
            keywords += keyword['keyword_or_phrase'] + \
                                                    keyword['explanation']

    text = request.content + keywords + queries
    vector = generate_embeddings(text, model, tokenizer)

    return ProcessedIndexRequest(
        content  = request.content,
        vector   = vector.tolist(),
        queries  = request.queries,
        keywords = request.keywords_or_phrases,
        chunk_id = request.chunk_id
    )

# Функция для преобразования объектов от запроса на индексацию
def processSearch(request: SearchRequest) -> ProcessedSearchRequest:
    vector = generate_embeddings(request.text, model, tokenizer)
    return ProcessedSearchRequest(
        content   = request.text,
        vector    = vector.tolist(),
        top_k     = request.top_k,
        filter_by = request.filter_by,
        keywords  = request.keywords
    )
