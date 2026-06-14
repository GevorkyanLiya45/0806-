import pytest
from mainnew import validate_password, filter_positive_numbers

# Тесты для валидации пароля (12 кейсов)
@pytest.mark.parametrize("pwd, expected", [
    ("Pass1234", True),      # TC-01: Корректный
    ("StrongPass1", True),   # TC-02: Длинный
    ("12345678", False),     # TC-03: Нет букв
    ("ABCdefgh", False),     # TC-04: Нет цифр
    ("Pass 123", False),     # TC-05: Пробел
    ("P1a", False),          # TC-06: Короче 8
    ("P1a2b3c4", True),      # TC-07: Граница 8
    ("12345678Abc", True),   # TC-08: Длинный валидный
    ("no_digits_!", False),  # TC-09: Нет цифр
    ("password!!!", False),  # TC-10: Нет цифр
    ("12345678!!!", False),  # TC-11: Нет букв
    ("Passw0rd", True)       # TC-07: Граница 8
])
def test_validate(pwd, expected):
    assert validate_password(pwd) == expected

# Тесты для фильтрации (12 кейсов)
@pytest.mark.parametrize("inp, out", [
    ("1, 5, 10", [1.0, 5.0, 10.0]),  # TC-01
    ("-1, -5", []),                  # TC-02
    ("0, 0", []),                    # TC-03
    ("0.5, 2.5", [0.5, 2.5]),        # TC-04
    ("1, -2, 3", [1.0, 3.0]),        # TC-05
    ("a, b, c", []),                 # TC-06
    ("1, a, 2, b", [1.0, 2.0]),      # TC-07
    ("1000000", [1000000.0]),        # TC-08
    (" ", []),                       # TC-09
    ("", []),                        # TC-10
    ("-0.5, 0.5", [0.5]),            # TC-11
    ("123", [123.0])                 # TC-12
])
def test_filter(inp, out):
    assert filter_positive_numbers(inp) == out

# Дополнительные тесты на ошибки (TypeError)
def test_type_errors():
    with pytest.raises(TypeError):
        validate_password(123)
    with pytest.raises(TypeError):
        filter_positive_numbers(123)