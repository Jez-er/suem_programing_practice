# Підхід А: без обробки помилок
# total = float(input("Сума замовлення: "))
# cups = int(input("Кількість чашок: "))
# print(f"Середня ціна: {total / cups:.2f} грн")

# Підхід Б: з обробкою помилок
try:
    total = float(input("Сума замовлення: "))
    cups = int(input("Кількість чашок: "))
    average = total / cups
except ValueError:
    print("Помилка: потрібно ввести число")
except ZeroDivisionError:
    print("Помилка: чашок не може бути нуль")
else:
    print(f"Середня ціна: {average:.2f} грн")
finally:
    print("Розрахунок завершено")