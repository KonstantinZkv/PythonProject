def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список словарей по значению ключа state"""

    return [transaction for transaction in transactions if transaction.get("state") == state]
