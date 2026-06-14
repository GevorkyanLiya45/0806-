def validate_password(password: str) -> bool:
    """Проверяет пароль на соответствие требованиям безопасности."""
    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")
    
    # Требования: минимум 8 символов, цифра, буква, нет пробелов
    if len(password) < 8: 
        return False 
    if " " in password: 
        return False
    if not any(c.isdigit() for c in password): 
        return False
    if not any(c.isalpha() for c in password): 
        return False
    return True

def filter_positive_numbers(input_str: str) -> list:
    """Фильтрует строку, возвращая список положительных чисел."""
    if not isinstance(input_str, str):
        raise TypeError("Входные данные должны быть строкой")
    
    items = input_str.split(',')
    result = []
    for item in items:
        # Пропускаем пустые элементы
        if not item.strip():
            continue
        try:
            val = float(item.strip())
            # Оставляем только строго положительные числа
            if val > 0:
                result.append(val)
        except ValueError:
            # Игнорируем всё, что нельзя превратить в число
            continue
    return result