import random


def filter_by_currency(transactions, currency):
    """Генератор, который фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой транзакции."""
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start=1, stop=9999999999999999):
    """Генерирует номер карты в диапазоне и приводит в корректный формат."""
    while True:
        new_number = random.randint(start, stop)
        new_number_str = str(new_number)
        correct_len_number = 16 - len(new_number_str)
        generated_number = "0" * correct_len_number + new_number_str
        yield f"{generated_number[:4]} {generated_number[4:8]} {generated_number[8:12]} {generated_number[12:]}"
