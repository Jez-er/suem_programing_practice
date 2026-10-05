"""Практична робота 3. Індивідуальне завдання.
Варіант 5: квадратне рівняння.
Виконала: Черненко А. Д., група КІТ-52
"""
import math

try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
except ValueError:
    print("Помилка: a, b, c мають бути числами")
else:
    if a == 0 and b == 0:
        print("Це не рівняння: a і b не можуть бути одночасно нульовими")
    else:
        kind = "лінійне" if a == 0 else "квадратне"
        print(f"Тип рівняння: {kind}")

        if a == 0:
            print(f"x = {-c / b:.2f}")
        else:
            d = b ** 2 - 4 * a * c
            print(f"Дискримінант: {d:.2f}")
            if d > 0:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                print(f"Два корені: x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif d == 0:
                x = -b / (2 * a)
                print(f"Один корінь: x = {x:.2f}")
            else:
                print("Дійсних коренів немає")