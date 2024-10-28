import json
from datasets import Dataset
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm


# Загрузка предварительно обученной модели E5 и токенизатора
model = AutoModel.from_pretrained("./multilingual-e5-base")
tokenizer = AutoTokenizer.from_pretrained("./multilingual-e5-base")

# Функция для токенизации данных
def tokenize_function(examples):
    # Преобразуем сразу в тензоры и возвращаем нужные данные
    tokenized = tokenizer(examples['query'], examples['content'], padding="max_length", truncation=True, return_tensors='pt')
    return {
        'input_ids': tokenized['input_ids'],
        'attention_mask': tokenized['attention_mask']
    }

# Загрузка данных для файнтюнинга
def load_finetune_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return Dataset.from_list(data)

# Путь к подготовленному датасету
dataset_file = 'finetune_dataset.json'
dataset = load_finetune_dataset(dataset_file)

# Токенизация данных
tokenized_dataset = dataset.map(tokenize_function)

# Создание DataLoader с преобразованием в тензоры
def collate_fn(batch):
    # Преобразуем input_ids и attention_mask из списков в тензоры
    input_ids = torch.cat([torch.tensor(item['input_ids']) for item in batch], dim=0)
    attention_mask = torch.cat([torch.tensor(item['attention_mask']) for item in batch], dim=0)
    return {'input_ids': input_ids, 'attention_mask': attention_mask}


train_dataloader = DataLoader(tokenized_dataset, batch_size=8, shuffle=True, collate_fn=collate_fn)

# Определение функции потерь на основе косинусного сходства
cosine_similarity = nn.CosineSimilarity(dim=1)
loss_fn = nn.MSELoss()  # Используем MSE для оптимизации косинусного расстояния

# Определяем оптимизатор
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

# Функция для обучения модели с отображением прогресса
def train(model, dataloader, optimizer, epochs=3, log_interval=10):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        batch_count = 0
        # Используем tqdm для удобного отображения прогресса по эпохе
        progress_bar = tqdm(dataloader, desc=f"Epoch {epoch + 1}", leave=False)

        for batch in progress_bar:
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(model.device)
            attention_mask = batch['attention_mask'].to(model.device)

            # Получаем эмбеддинги для query и content
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            embeddings = outputs.last_hidden_state[:, 0, :]  # Используем эмбеддинги [CLS]-токена

            # Разделяем эмбеддинги на query и content
            half_size = embeddings.size(0) // 2
            query_embeddings = embeddings[:half_size]
            content_embeddings = embeddings[half_size:]

            # Вычисляем косинусное сходство между запросами и параграфами
            similarities = cosine_similarity(query_embeddings, content_embeddings)
            labels = torch.ones(similarities.size()).to(model.device)  # Позитивные примеры имеют метку 1

            # Вычисляем loss и делаем шаг оптимизации
            loss = loss_fn(similarities, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            batch_count += 1

            # Отображаем средний loss каждые log_interval батчей
            if batch_count % log_interval == 0:
                avg_batch_loss = total_loss / batch_count
                progress_bar.set_postfix({'Average Batch Loss': avg_batch_loss})

        avg_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch + 1}, Average Loss: {avg_loss}")

    print("Training complete!")

# Перемещаем модель на GPU, если доступно
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Запуск тренировки
train(model, train_dataloader, optimizer)

# Сохранение модели
model.save_pretrained("./e5_finetuned")
tokenizer.save_pretrained("./e5_finetuned")

