import math

# 1. Середнє арифметичне трьох чисел: a = 7, b = 12, c = 20
first_task_a = 7
first_task_b = 12
first_task_c = 20

average = first_task_a + first_task_b + first_task_c / 3
print(f"1. Середнє арифметичне: {average:.2f}")

# 2. Площа трапеції: a = 8, b = 12, h = 5
second_task_a = 8
second_task_b = 12
second_task_h = 5

trapezoid_area = ((second_task_a + second_task_b) / 2) * second_task_h
print(f"2. Площа трапеції: {trapezoid_area:.2f}")

# 3. Довжина кола та площа круга для r = 4.5
third_task_r = 4.5

circumference = 2 * math.pi * third_task_r
area = math.pi * third_task_r ** 2
print(f"3. Довжина кола: {circumference:.2f} | Площа круга: {area:.2f}")

# 4. Гіпотенуза прямокутного трикутника для катетів 3 і 4
fourth_task_a_leg = 3
fourth_task_b_leg = 4

hypotenuse = math.sqrt(fourth_task_a_leg ** 2 + fourth_task_b_leg ** 2)
print(f"4. Гіпотенуза: {hypotenuse:.2f}")

# 5. Години, хвилини, секунди у 10 000 секундах
fifth_task_total_seconds = 10000

hours = fifth_task_total_seconds // 3600
remainder = fifth_task_total_seconds % 3600
minutes = remainder // 60
seconds = remainder % 60
print(f"5. {hours} год {minutes} хв {seconds} с")