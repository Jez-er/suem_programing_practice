# Підхід А: вкладені умови
# try:
#     age = int(input("Вік: "))
#     has_card = input("Студентський? (так/ні): ") == "так"
# except ValueError:
#     print("Помилка: вік має бути числом")
# else:
#     if age < 18:
#         if has_card:
#             price = 60
#         else:
#             price = 80
#     else:
#         if has_card:
#             price = 90
#         else:
#             price = 150
#     print(f"Ціна квитка: {price} грн")


# Підхід Б: складені умови та elif
try:
    age = int(input("Вік: "))
    has_card = input("Студентський? (так/ні): ") == "так"
except ValueError:
    print("Помилка: вік має бути числом")
else:
    if age < 18 :
        price = 80
    elif age < 18 and has_card:
        price = 60
    elif has_card:
        price = 90
    else:
        price = 150
    print(f"Ціна квитка: {price} грн")
