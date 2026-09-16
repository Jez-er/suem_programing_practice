# Підхід А: склеювання рядків через +
	# drink = "Латте"
	# price = 55.0
	# cups = 3
	# total = price * cups
	# print("Замовлення: " + drink + " x " + str(cups) + " = " + str(total) + " грн")

# Підхід Б: аргументи print через кому
drink = "Латте"
price = 55.0
cups = 3
total = price * cups
a = '"Замовлення:",drink,"x",cups,"=",total,"грн"'
print(a.__len__())

# Підхід В: аргументи print через f-рядки
# drink = "Латте"
# price = 55.0
# cups = 3
# total = price * cups
# print(f"Замовлення: {drink} x {cups} = {total} грн")