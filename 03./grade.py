# Практична 3, завдання 2: бали -> оцінка
try:
    points = int(input("Кількість балів (0-100): "))
except ValueError:
    print("Помилка: потрібне ціле число")
else:
    if points < 0 or points > 100:
        print("Бали мають бути від 0 до 100")
    elif points >= 60:
        print("Задовільно (D-E)")
    elif points >= 74:
      print("Добре (B-C)")
    elif points >= 90:
      print("Відмінно (A)")
    else:
        print("Незадовільно (FX-F)")
        
