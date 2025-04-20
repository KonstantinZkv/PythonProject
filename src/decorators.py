from functools import wraps


def log(filename=None):
    """Декоратор для логирования выполнения функций"""

    def wrapper(func):

        @wraps(func)
        def inner(*args, **kwargs):
            """Функция, ведущая запись лога"""
            try:
                result = func(*args, **kwargs)  # Вызываем функцию один раз
                message = (
                    f"\n{func.__name__} Запуск Ok. Входные параметры: {args}, {kwargs}."
                    f"\n{func.__name__} Завершение. Результат: {result}."
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                else:
                    print(message)
                return result
            except Exception as error:
                error_message = f"\n{func.__name__} Ошибка: {error}. Входные параметры: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)
                raise  # Пробрасываем исключение дальше

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
