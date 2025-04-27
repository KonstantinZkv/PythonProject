import os

import pandas as pd

current_file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(current_file_path)
project_root = os.path.dirname(src_dir)
data_dir = os.path.join(project_root, "data")
file_path_csv = os.path.join(data_dir, "transactions.csv")
file_path_xlsx = os.path.join(data_dir, "transactions_excel.xlsx")


def read_csv_transactions(file_path_csv):
    """Функция читает транзакции из CSV-файла и возвращает их в виде списка словарей"""
    try:
        if not os.path.exists(file_path_csv):
            raise FileNotFoundError(f"Файл {file_path_csv} не найден")
        df = pd.read_csv(file_path_csv, sep=";")
        data = df.to_dict("records")
        return [row for row in data]
    except FileNotFoundError as e:
        print(f"Ошибка! Файл не найден.: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка! {str(e)}")
        return []


def read_excel_transactions(file_path_xlsx):
    """Функция читает транзакции из XLSX-файла и возвращает их в виде списка словарей"""
    try:
        if not os.path.exists(file_path_xlsx):
            raise FileNotFoundError(f"Файл {file_path_xlsx} не найден")

        print(f"Попытка прочитать файл: {file_path_xlsx}")
        df = pd.read_excel(file_path_xlsx)

        data = df.to_dict("records")
        return [row for row in data]
    except FileNotFoundError as e:
        print(f"Ошибка! Файл не найден.: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка! {str(e)}")
        return []


# print(read_excel_transactions(file_path_xlsx))
# print(read_csv_transactions(file_path_csv))
