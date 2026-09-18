from datetime import date

"""Практична робота 1. Індивідуальне завдання.
Варіант 7: фільм.
Виконав: Черненко А., група КІТ-52"""

# --- 1. Дані об'єкта у змінних чотирьох типів ---
title = "Тіні забутих предків"            # str: назва
year = 1965                 # int: рік випуску
rating = 8.5               # float: рейтинг
is_available = True         # bool: чи є в прокаті

# --- 2. Вивід значень і їхніх типів ---
print("Назва:", title, "|", type(title))
print("Рік випуску:", year, "|", type(year))
print("Рейтинг:", rating, "|", type(rating))
print("У прокаті:", is_available, "|", type(is_available))

# --- 3. Обчислення з двома числовими змінними ---
actual_year = date.today().year
age = actual_year - year
print("Вік фільму:", age, "рік/років")
print("Рейтинг у відцотках:", int(rating * 10), "%")

# --- 4. Перетворення типів ---
print("Рейтинг як рядок:", str(rating) + " балів")
print("Ціла частина рейтингу:", int(rating))
print("Рік як float:", float(year))

# --- 5. Порівняння -> bool ---
is_new = year > 2000
print("Свіжий фільм:", is_new, "|", type(is_new))
print("Рейтинг більший за 7:", rating > 7, "|", type(rating > 7))