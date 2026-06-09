def validate_password(password):
    if len(password) < 3: return False 
    if not any(char.isdigit() for char in password): return False
    if not any(char.isalpha() for char in password): return False
    if " " in password: return False
    return True

def filter_positive_numbers(input_str):
    try:
        items = input_str.split(',')
        result = []
        for item in items:
            val = float(item.strip())
            if val >= 0: 
                result.append(val)
        return result
    except:
        return "Ошибка ввода"