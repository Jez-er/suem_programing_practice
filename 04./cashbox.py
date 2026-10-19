# Практична 4, завдання 2: каса за день
print("Вводьте суми чеків. 0 — закрити касу.")
total = 0
count = 0
biggest = 0
while True:
	try:
		check = float(input("Чек, грн: "))
	except ValueError:
		print("  Це не число, повторіть")
		continue
	if check == 0:
		break
	if check < 0:
		print("  Сума не може бути від'ємною")
		continue
	total += check
	count += 1
	if check > biggest:
		biggest = check
		if count > 0:
			print(f"Чеків: {count}")
			print(f"Виторг: {total:.2f} грн")
			print(f"Середній чек: {total / count:.2f} грн")
			print(f"Найбільший чек: {biggest:.2f} грн")
		else:
			print("За день не було жодного чека")
