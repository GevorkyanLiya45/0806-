import tkinter as tk
from tkinter import messagebox

# --- ЛОГИКА (Функции) ---
def validate_password(password):
    # Минимум 8 символов, есть цифра, есть буква, нет пробелов
    if len(password) < 8: return False
    if not any(char.isdigit() for char in password): return False
    if not any(char.isalpha() for char in password): return False
    if " " in password: return False
    return True

def filter_positive_numbers(input_str):
    # Превращаем строку "1, -2, 3" в список чисел и фильтруем
    try:
        items = input_str.split(',')
        result = []
        for item in items:
            val = float(item.strip())
            if val > 0:
                result.append(val)
        return result
    except:
        return "Ошибка ввода"

# --- ГРАФИЧЕСКИЙ ИНТЕРФЕЙС (GUI) ---
def run_app():
    root = tk.Tk()
    root.title("Data Validator & Filter")
    root.geometry("300x250")

    # Секция пароля
    tk.Label(root, text="Введите пароль:").pack(pady=5)
    pwd_entry = tk.Entry(root)
    pwd_entry.pack()
    tk.Button(root, text="Проверить пароль", command=lambda: messagebox.showinfo("Результат", 
        f"Валиден: {validate_password(pwd_entry.get())}")).pack(pady=5)

    # Секция фильтра
    tk.Label(root, text="Числа (через запятую):").pack(pady=5)
    list_entry = tk.Entry(root)
    list_entry.pack()
    tk.Button(root, text="Отфильтровать", command=lambda: messagebox.showinfo("Результат", 
        f"Положительные: {filter_positive_numbers(list_entry.get())}")).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_app()