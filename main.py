from src.masks import get_mask_account, get_mask_card_number

"""Получаем данные от пользователя"""

card_number = input("Введите номер карты: ")
print(get_mask_card_number(card_number))

account_number = input("Введите номер счёта: ")
print(get_mask_account(account_number))
