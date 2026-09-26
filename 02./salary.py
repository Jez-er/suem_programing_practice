"""Практична робота 2. Індивідуальне завдання.
Варіант 10: розрахунок зарплати за годинами.
Виконав: Черненко Андрій, група КІТ-52
"""

MINIMUM_WAGE = 8647.0   
HOURS_PER_DAY = 8       

print("=== Розрахунок зарплати за годинами ===")

try:
    hours = float(input("Відпрацьовано годин: "))
    rate = float(input("Ставка за годину, грн: "))
    tax_percent = float(input("Ставка податку, %: "))

    accrued = hours * rate                     
    tax_amount = accrued * tax_percent / 100     
    net_pay = accrued - tax_amount

    full_days = hours // HOURS_PER_DAY    
    rest_hours = hours % HOURS_PER_DAY        

    is_above_minimum = net_pay > MINIMUM_WAGE  

    print(f"Нараховано:      {accrued:.2f} грн")
    print(f"Податок:         {tax_amount:.2f} грн")
    print(f"На руки:         {net_pay:.2f} грн")
    print(f"Відпрацьовано:   {full_days:.0f} повних днів по {HOURS_PER_DAY} год, залишок {rest_hours:.1f} год")
    print(f"На руки більше мінімалки ({MINIMUM_WAGE:.2f} грн): {is_above_minimum}")

except ValueError:
    print("Помилка: усі значення мають бути числами")