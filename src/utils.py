import json
import os
from typing import Dict, List

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "../data/operations.json")


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает транзакции из JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что data — это список
            if isinstance(data, list):
                return data
            return []

    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON из файла: {file_path}")
        return []
