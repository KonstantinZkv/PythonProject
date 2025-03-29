from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_numbers):
    """Тестирование функции маскировки номера банковской карты."""
    for card_number, expected in card_numbers:
        assert get_mask_card_number(card_number) == expected


def test_get_mask_account(account_numbers):
    """Тестирование функции маскировки номера банковского счета."""
    for account_number, expected in account_numbers:
        assert get_mask_account(account_number) == expected
