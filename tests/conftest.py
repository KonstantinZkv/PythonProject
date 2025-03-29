import pytest


@pytest.fixture
def card_numbers():
    """Фикстура для тестирования маскировки номеров карт."""
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("4000123456789010", "4000 12** **** 9010"),
        ("5555555555554444", "5555 55** **** 4444"),
    ]


@pytest.fixture
def account_numbers():
    """Фикстура для тестирования маскировки номеров счетов."""
    return [
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("98765432109876543210", "**3210"),
    ]


@pytest.fixture
def transactions():
    """Фикстура для тестирования фильтрации и сортировки транзакций."""
    return [
        {"date": "2024-03-11T02:26:18.671407", "state": "EXECUTED"},
        {"date": "2024-03-10T02:26:18.671407", "state": "CANCELED"},
        {"date": "2024-03-09T02:26:18.671407", "state": "EXECUTED"},
        {"date": "2024-03-08T02:26:18.671407", "state": "PENDING"},
    ]


@pytest.fixture
def date_formats():
    """Фикстура для тестирования различных форматов дат."""
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2022-01-01T00:00:00.000000", "01.01.2022"),
        ("2021-07-15T15:30:00.000000", "15.07.2021"),
        ("2020-02-29T12:00:00.000000", "29.02.2020"),  # Високосный год
    ]
