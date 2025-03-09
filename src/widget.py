from src.masks import get_mask_card_number

def mask_account_card(string: str) -> tuple[str, str]:
    """Функция обработки информации о картах и счетах"""

    string_split = string.split()
    name_card_or_score  = ''.join(string_split[:-1])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score

# test = "Visa Platinum 7000792289606361" #для теста
# name_card, number_card = mask_account_card(test)
# masked_number = get_mask_card_number(number_card)
# print(f'{name_card}: {masked_number}')