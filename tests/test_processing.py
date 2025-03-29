from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transactions):
    """Тестирование функции фильтрации транзакций по состоянию."""
    executed_transactions = filter_by_state(transactions, "EXECUTED")
    assert len(executed_transactions) == 2
    assert all(tx["state"] == "EXECUTED" for tx in executed_transactions)

    canceled_transactions = filter_by_state(transactions, "CANCELED")
    assert len(canceled_transactions) == 1
    assert canceled_transactions[0]["state"] == "CANCELED"

    pending_transactions = filter_by_state(transactions, "PENDING")
    assert len(pending_transactions) == 1
    assert pending_transactions[0]["state"] == "PENDING"


def test_sort_by_date(transactions):
    """Тестирование функции сортировки транзакций по дате."""
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions[0]["date"] == "2024-03-11T02:26:18.671407"
    assert sorted_transactions[1]["date"] == "2024-03-10T02:26:18.671407"
    assert sorted_transactions[2]["date"] == "2024-03-09T02:26:18.671407"
    assert sorted_transactions[3]["date"] == "2024-03-08T02:26:18.671407"
