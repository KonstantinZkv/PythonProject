import re
from collections import Counter
from typing import Any, Dict, List


def filter_transactions(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    filtered_list_transactions = []

    pattern = re.compile(search_string, re.IGNORECASE)

    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            filtered_list_transactions.append(transaction)

    return filtered_list_transactions


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, значения — это количество в каждой категории.
    Категории операций хранятся в поле description
    """

    # Собираем все описания (description) из операций, которые есть в заданном списке категорий
    description_list = [
        transaction.get("description") for transaction in transactions if transaction.get("description") in categories
    ]

    # Используем Counter для подсчета
    description_counts = Counter(description_list)

    # Преобразуем Counter в обычный словарь и добавляем категории с нулевым количеством
    result = {category: description_counts.get(category, 0) for category in categories}

    return result
