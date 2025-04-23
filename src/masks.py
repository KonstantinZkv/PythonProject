import logging
import os
from typing import Union

logger = logging.getLogger(__name__)


script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(script_dir, "../logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = logging.FileHandler(os.path.join(log_dir, "masks.log"), encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    logger.info(f"Получаем данные карты")
    if len(str(card_number)) != 16 or not str(card_number.isdigit()):
        logger.error(f"Некорректный номер карты: {card_number}")
        raise ValueError(f"Некорректный номер карты")

    str_card = str(card_number)
    number = f"{str_card[:4]} {str_card[5:7]}** **** {str_card[-4:]}"
    logger.info(f"Замаскированный номер карты {number}")
    return number


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""
    logger.info(f"Получаем номер банковского счета")
    if len(str(account_number)) != 20 or not str(account_number.isdigit()):
        logger.error(f"Некорректный номер счета")
        raise ValueError("Некорректный номер счета")

    str_account_number = str(account_number)
    number = f"**{str_account_number[-4:]}"
    logger.info(f"Возращаем маску счета {number}")
    return number


if __name__ == "__main__":
    # Код для тестирования функций
    card_number = input("Введите номер карты: ")
    print(get_mask_card_number(card_number))

    account_number = input("Введите номер счёта: ")
    print(get_mask_account(account_number))
