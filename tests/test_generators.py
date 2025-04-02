import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        # Другие транзакции...
    }
]


@pytest.mark.parametrize("currency, expected_count", [
    ('USD', 1),
    ('EUR', 1),
    ('GBP', 0),  # Не существует в списке
])
def test_filter_by_currency(currency, expected_count):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert len(filtered_transactions) == expected_count


@pytest.mark.parametrize("input_transactions, expected_descriptions", [
    (transactions, [
        'Перевод организации',
        'Перевод со счета на счет',
    ]),
    ([], []),  # Пустой список транзакций
])
def test_transaction_descriptions(input_transactions, expected_descriptions):
    descriptions = list(transaction_descriptions(input_transactions))
    assert descriptions == expected_descriptions


def test_card_number_generator():
    gen = card_number_generator()

    generated_numbers = [next(gen) for _ in range(5)]

    for number in generated_numbers:
        assert len(number) == 19  # Проверяем формат XXXX XXXX XXXX XXXX