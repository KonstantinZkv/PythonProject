import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """Функция обработки информации о картах и счетах"""

    string_split = string.split()
    name_card_or_score = " ".join(string_split[:-1])
    number_card_or_score = string_split[-1]
    if name_card_or_score == "Счет":
        return f"{name_card_or_score} {get_mask_account(number_card_or_score)}"
    else:
        return f"{name_card_or_score} {get_mask_card_number(number_card_or_score)}"


# test = "Visa Platinum 7000792289606361" #для теста
# print(mask_account_card(test))
#
# test = "Maestro 7000792289606361"
# print(mask_account_card(test))
#
# test = "Счет 35383033474447895560"
# print(mask_account_card(test))
#
# test = "Счет 73654108430135874305"
# print(mask_account_card(test))


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
