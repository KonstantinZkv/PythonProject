from src.masks import get_mask_account, get_mask_card_number

from config import PATH_TO_CSV, PATH_TO_EXCEL, PATH_TO_JSON
from src.csv_xlsx_reader import read_csv_transactions, read_excel_transactions
from src.processing import filter_by_state, sort_by_date
from src.transaction_filter import count_operations_by_category, filter_transactions
from src.utils import load_transactions
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency


def format_transaction(transaction):
    """Форматирует транзакцию для вывода в заданном формате"""
    try:
        # Основные данные
        date = get_date(transaction.get("date", ""))
        description = transaction.get("description", "Описание отсутствует")

        # Обработка карт/счетов
        from_account = mask_account_card(str(transaction["from"])) if "from" in transaction else ""
        to_account = mask_account_card(str(transaction.get("to", "Получатель не указан")))

        # Улучшенная обработка суммы
        amount_display = "не указана"
        currency = ""

        # Проверяем разные варианты структуры суммы
        if "amount" in transaction:  # Прямое поле amount
            amount = transaction["amount"]
            currency = transaction.get("currency", "")
        else:  # Стандартная структура с operationAmount
            operation_amount = transaction.get("operationAmount", {})
            if isinstance(operation_amount, dict):
                amount = operation_amount.get("amount")
                currency_data = operation_amount.get("currency", {})
                currency = currency_data.get("code", "") if isinstance(currency_data, dict) else str(currency_data)

        # Форматируем сумму
        if "amount" in locals() and amount not in [None, ""]:
            try:
                amount_num = float(amount)
                amount_display = f"{amount_num:,.2f}".replace(",", " ").replace(".00", "")
            except (ValueError, TypeError):
                amount_display = str(amount).strip()

        # Формируем результат
        result = f"{date} {description}\n"
        if from_account:
            result += f"{from_account} -> "
        result += f"{to_account}\n"
        result += f"Сумма: {amount_display} {currency}" if currency else f"Сумма: {amount_display}"

        return result

    except Exception as e:
        print(f"Ошибка форматирования транзакции: {e}")
        return f"Не удалось отформатировать транзакцию: {transaction}"


def show_statistics(transactions):
    """Выводит статистику по операциям, используя coun_description"""
    common_categories = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод со счета на счет",
        "Открытие вклада",
        "Пополнение счета",
    ]

    stats = count_operations_by_category(transactions, common_categories)
    print("\nСтатистика операций по категориям:")
    for category, count in stats.items():
        print(f"{category}: {count}")


def main():
    print(
        """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )

    # Выбор файла
    while True:
        file_type = input("Выберете номер операции: ").strip()
        if file_type == "1":
            print("\nДля обработки выбран JSON-файл.")
            break
        elif file_type == "2":
            print("\nДля обработки выбран CSV-файл.")
            break
        elif file_type == "3":
            print("\nДля обработки выбран XLSX-файл.")
            break
        else:
            print("Пожалуйста, введите корректный номер: 1,2 или 3")

    # Загрузка данных
    transactions = []

    try:
        if file_type == "1":
            transactions = load_transactions(PATH_TO_JSON)
        elif file_type == "2":
            transactions = read_csv_transactions(PATH_TO_CSV)
        elif file_type == "3":
            transactions = read_excel_transactions(PATH_TO_EXCEL)
    except Exception as e:
        print(f"\nОшибка при загрузке файла: {e}")
        transactions = []  # Явно указываем пустой список

    # Фильтрация по статусу
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Ваш выбор: ").upper().strip()

        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, state)
            print(f"\nОперации отфильтрованы по статусу '{state}'")
            break
        else:
            print(f'\nСтатус операции "{state}" недоступен')

    # Сортировка по дате
    while True:
        sort_choice = input("\nОтсортировать операции по дате? (Да/Нет): ").lower().strip()
        if sort_choice in ["да", "нет"]:
            break

    if sort_choice == "да":
        while True:
            sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower().strip()
            if sort_order == "по возрастанию":
                transactions = sort_by_date(transactions)
                break
            elif sort_order == "по убыванию":
                transactions = sort_by_date(transactions, False)
                break

        # Фильтрация по ключевому слову
        while True:
            filter_word = input("\nОтфильтровать список транзакций по слову в описании? (Да/Нет): ").lower().strip()
            if filter_word in ["да", "нет"]:
                break

        if filter_word == "да":
            keyword = input("Введите слово для фильтрации (Перевод с карты на карту, Перевод со счета на счет): ").strip()
            transactions = filter_transactions(transactions, keyword)

        else:
            print("Не корректные данные")

        # Фильтрация по рублевым транзакциям
        while True:
            filter_word = input("\nВыводить только RUB транзакции? (Да/Нет): ").lower().strip()
            if filter_word in ["да", "нет"]:
                break

        if filter_word == "да":
            transactions = list(filter_by_currency(transactions, "RUB"))
        else:
            user_currency = (input("Введите слово для фильтрации валюты: USD, EUR: ")).upper().strip()
            transactions = list(filter_by_currency(transactions, user_currency))

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in transactions:
            print(format_transaction(transaction))
            print("-" * 50)

    if transactions:  # Только если есть транзакции
        show_statistics(transactions)



if __name__ == "__main__":
    main()