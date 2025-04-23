import json
import unittest
from unittest.mock import MagicMock, patch

from src.external_api import currency_exchange, transaction_info


@patch("requests.get")
def test_currency_exchange_success(mock_get):
    # Настраиваем mock-объект, чтобы возвращать статус 200 и JSON-ответ
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 100}  # Пример результата конвертации
    mock_get.return_value = mock_response

    # Передаем словарь в функцию
    data = {"output_code": "RUB", "input_code": "USD", "amount": 10}
    result = currency_exchange(data)

    # Простой assert для проверки результата
    assert result == {"result": 100}, "Expected result to be {'result': 100}"


class TestTransactionInfo(unittest.TestCase):

    @patch("src.external_api.currency_exchange")
    def test_transaction_info_with_rub(self, mock_currency_exchange):
        # Тестируем случай, когда валюта уже в RUB
        transaction = [{"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}]

        result = transaction_info(transaction)
        self.assertEqual(result, 100.0, "Expected result to be 100.0")

    @patch("src.external_api.currency_exchange")
    def test_transaction_info_with_non_rub(self, mock_currency_exchange):
        # Настраиваем mock для функции currency_exchange
        mock_currency_exchange.return_value = {"result": 150.0}

        transaction = [{"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}]

        result = transaction_info(transaction)
        self.assertEqual(result, 150.0, "Expected result to be 150.0")

    @patch("src.external_api.currency_exchange")
    def test_transaction_info_empty_transaction(self, mock_currency_exchange):
        # Тестируем случай с пустой транзакцией
        transaction = []

        result = transaction_info(transaction)
        self.assertEqual(result, 0.0, "Expected result to be 0.0")

    @patch("src.external_api.currency_exchange")
    def test_transaction_info_with_unexpected_currency(self, mock_currency_exchange):
        # Тестируем случай с неожиданной валютой
        mock_currency_exchange.return_value = {"result": 200.0}

        transaction = [{"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}]

        result = transaction_info(transaction)
        self.assertEqual(result, 200.0, "Expected result to be 200.0")

    @patch("requests.get")
    def test_currency_exchange_missing_keys(self, mock_get):
        # Тестируем случай, когда отсутствуют необходимые ключи
        data = {"output_code": "RUB", "amount": 10}  # input_code отсутствует
        result = currency_exchange(data)
        self.assertEqual(result, {}, "Expected result to be an empty dictionary due to missing keys")


if __name__ == "__main__":
    unittest.main()
