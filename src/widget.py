import re

from src.masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция обработки информации о картах и счетах"""

    string_split = string.split()
    name_card_or_score = "".join(string_split[:-1])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score


# test = "Visa Platinum 7000792289606361" #для теста
# name_card, number_card = mask_account_card(test)
# masked_number = get_mask_card_number(number_card)
# print(f'{name_card}: {masked_number}')


def get_date(input_string: str) -> str:
    """Функция изменения формата даты"""
    date_string = ""
    for item in input_string:
        clean_string = re.findall("[0-9]", item)
        if clean_string:
            date_string += "".join(clean_string)
    return f"{date_string[6:8]}.{date_string[4:6]}.{date_string[:4]}"


# test = "2024-03-11T02:26:18.671407" #для теста
# print(get_date(test))
