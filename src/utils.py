import json
import logging
import os
from typing import Dict, List

logger = logging.getLogger(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(script_dir, "../logs")
log_file_path = os.path.join(log_dir, "utils.log")
os.makedirs(log_dir, exist_ok=True)


file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
console_handler = logging.StreamHandler()
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

file_path = os.path.join(script_dir, "../data", "operations.json")


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает транзакции из JSON-файла.
    """
    logger.info("Получаем данные из файла")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что data — это список
            logger.info("Проверяем, что data — это список")
            if isinstance(data, list):
                return data
            return []

    except FileNotFoundError as ex:
        logger.error(f"Файл не найден по пути: {file_path}, ошибка: {ex}")
        return []
    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка при декодировании JSON из файла: {file_path}, ошибка: {ex}")
        return []


if __name__ == "__main__":

    print(f"Путь к файлу: {file_path}")

    operations = load_transactions(file_path)

    if operations:
        print("Операции успешно загружены:")
        for operation in operations:
            print(operation)
    else:
        print("Не удалось загрузить операции.")
