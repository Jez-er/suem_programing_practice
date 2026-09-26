PRICE = 45.0

drink = input("Назва напою: ")
cups = float(input("Скільки чашок? "))


total = cups * PRICE

print(f"Замовлення: {drink} x {cups}")
print(f"До сплати: {total:.2f} грн")
print(f"Знижка: {total * 0.1:.2f} грн")
print("-----------------------------")
print(f"Ціна однієї: {total / cups:.2f} грн")

x = 5
print(x ++ 1)
