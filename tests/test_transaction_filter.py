from src.transaction_filter import count_operations_by_category, filter_transactions


def test_no_match(transactions):
    """Тест, когда строка не найдена"""
    result = filter_transactions(transactions, r"Несуществующий текст")
    assert result == []


def test_empty_search_string(transactions):
    """Тест, должен вернуть все транзакции"""
    result = filter_transactions(transactions, "")
    assert result == transactions


def test_empty_categories(transactions):
    """Тест пустого списка словаря транзакций"""
    result = count_operations_by_category(transactions, [])
    assert result == {}


def test_no_matching_categories(transactions):
    """Тест несуществующей категории транзакций"""
    result = count_operations_by_category(transactions, ["Несуществующая категория"])
    assert result == {"Несуществующая категория": 0}


def test_missing_description_field():
    """Тест отсутствие поля description"""
    transactions = [{"id": 1, "no_description": "test"}, {"id": 2, "description": "Перевод организации"}]
    result = count_operations_by_category(transactions, ["Перевод организации"])
    assert result == {"Перевод организации": 1}