import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_string, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Счет 98765432109876543210", "Счет **3210"),
])
def test_mask_account_card(input_string, expected):
    """Тестирование функции обработки информации о картах и счетах."""
    assert mask_account_card(input_string) == expected


def test_get_date(date_formats):
    """Тестирование функции изменения формата даты."""
    for input_string, expected in date_formats:
        assert get_date(input_string) == expected
