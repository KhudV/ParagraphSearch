import json

def convert_to_finetune_format(input_file, output_file):
    # Загрузка данных из файла
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Список для хранения пар (query, content)
    pairs = []

    # Проход по всем записям
    for entry in data:
        try:
          content = entry.get('content', '').strip()
          queries = entry.get('queries', [])
        except:
          print("Error in entry:")
          print(entry)

        # Если есть запросы, создаем пары (query, content)
        if queries:
            for query in queries:
                if query:  # Проверка, что запрос не является None
                    pairs.append({
                        "query": query.strip(),
                        "content": content
                    })

    # Сохранение преобразованных данных в новый файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(pairs, f, ensure_ascii=False, indent=4)

    print(f"Data has been successfully converted and saved to {output_file}")

# Пример использования
input_file = './Data/search.parahraph.gazpromneft.json'
output_file = './Data/finetune_dataset.json'
convert_to_finetune_format(input_file, output_file)

