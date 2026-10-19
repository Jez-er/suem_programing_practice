# # Підхід А: while — сума парних від 2 до n
# try:
# 	n = int(input("n = "))
# except ValueError:
# 	print("Потрібне ціле число")
# else:
# 	total = 0
# 	k = 2
# 	while k <= n:
# 		total += k
# 		k += 2
# 	print(f"Сума парних до {n}: {total}")

# Підхід Б: for + range з кроком 2
try:
	n = int(input("n = "))
except ValueError:
	print("Потрібне ціле число")
else:
	total = 0
	for k in range(2, n + 1, 2):
		total += k
	print(f"Сума парних до {n}: {total}")
