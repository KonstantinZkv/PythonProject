import os
from typing import Dict, List, Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_exchange(data: Dict[str, Union[str, int, float]]) -> dict:
    """Функция конвертации валюты, принимает словарь с параметрами"""
    try:
        output_code = data.get("output_code")
        input_code = data.get("input_code")
        amount = data.get("amount")

        if output_code is None or input_code is None or amount is None:
            raise ValueError("Отсутствуют необходимые ключи в словаре")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={input_code}&from={output_code}&amount={amount}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()  # Возвращаем JSON-ответ
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")  # Генерируем исключение для ошибок

    except Exception as e:
        print(f"Ошибка в функции currency_exchange: {e}")
        return {}


def transaction_info(transaction: List[Dict]) -> float:
    """Вывод суммы транзакции"""
    if not transaction:  # Проверяем, является ли транзакция пустой
        return 0.0

    for item in transaction:
        currency_code = item["operationAmount"]["currency"]["code"]
        amount = float(item["operationAmount"]["amount"])

        if currency_code == "RUB":
            return amount

        convert = {"input_code": "RUB", "output_code": currency_code, "amount": amount}
        result_dict = currency_exchange(convert)

        # Проверяем, есть ли результат
        if "result" in result_dict:
            return float(result_dict["result"])

    return 0.0  # Возвращаем 0.0, если не нашли подходящую валюту


transaction = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
]

if __name__ == "__main__":
    result = transaction_info(transaction)
    print(result)
    print(type(result))
