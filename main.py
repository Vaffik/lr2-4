import math
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))
h = (x ** (y + 1) + math.e ** (y - x)) / (1 + x * abs(y - math.tan(z))) * (1 + abs(y - x)) + (abs(y - x) ** 2) / 2 - (abs(y - x) ** 3) / 3
print (f"h = {h}")