"""Практична робота 4. Індивідуальне завдання.
Варіант 3: накопичення на покупку.
Виконав: Черненко А.Д., група КІТ-52
"""
MONTHS_IN_TABLE = 6

while True:
    try:
        price = float(input("Ціна покупки, грн: "))
    except ValueError:
        print("  Потрібне число")
        continue
    if price > 0:
        break
    print("  Ціна має бути більшою за 0")

while True:
    try:
        deposit = float(input("Щомісячний внесок, грн: "))
    except ValueError:
        print("  Потрібне число")
        continue
    if deposit > 0:
        break
    print("  Внесок має бути більшим за 0")

saved = 0
months = 0
while saved < price:
    saved += deposit
    months += 1

print()
print(f"{'Місяців до покупки':<24}{months:>12}")
print(f"{'Буде накопичено':<24}{saved:>12.2f} грн")
print(f"{'Залишок після покупки':<24}{saved - price:>12.2f} грн")

print()
print(f"{'Місяць':<8}{'Накопичено, грн':>18}{'Залишилось, грн':>18}")
total = 0
for month in range(1, MONTHS_IN_TABLE + 1):
    total += deposit
    left = price - total
    if left < 0:
        left = 0
    print(f"{month:<8}{total:>18.2f}{left:>18.2f}")
