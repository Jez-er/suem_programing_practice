drink = "Capuccino"
price = 60.0
cups = 2.0
has_syrup = True

print("Drink:", drink, type(drink))
print("Price:", price, type(price))
print("Cups:", cups, type(cups))
print("Has Syrup:", has_syrup, type(has_syrup))

total = price * cups
print("To pay:", total, type(total))

price_text = str(price) + " UAH"
print(price_text, type(price_text))

cups_text = "5"
print(cups_text + cups_text)
print(float(cups_text) + float(cups_text))

print(price > 50, type(price > 50))
