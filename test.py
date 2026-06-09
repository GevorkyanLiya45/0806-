import unittest
from main import validate_password, filter_positive_numbers

class TestLogicChecker(unittest.TestCase):

    def test_password_validation(self):
        assert validate_password("P1a") == False, "Ошибка: пароль слишком короткий"
        assert validate_password("Pass1234") == True, "Ошибка: правильный пароль не прошел"

    def test_filter_numbers(self):
        result = filter_positive_numbers("1, -5, 0")
        assert 0 not in result, "Ошибка: 0 не должен быть в списке"
        assert result == [1.0], "Ошибка: список отфильтрован неверно"

if __name__ == '__main__':
    unittest.main()