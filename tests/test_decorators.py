import pytest

from src.decorators import log


def test_successful_execution_console_logging(capsys):
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)

    # Проверяем результат выполнения
    assert result == 5

    # Проверяем вывод в консоль
    console_view = capsys.readouterr()
    assert "add Запуск Ok. Входные параметры: (2, 3), {}" in console_view.out
    assert "add Завершение. Результат: 5" in console_view.out


def test_failed_execution_console_logging(capsys):
    """Тест ошибки выполнения с выводом в консоль"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # Проверяем вывод в консоль
    console_view = capsys.readouterr()
    assert "divide Ошибка: division by zero" in console_view.out
    assert "Входные параметры: (10, 0), {}" in console_view.out
