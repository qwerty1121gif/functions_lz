import math

r = float(input("Введите радиус круга: "))

area = math.pi * r**2
circumference = 2 * math.pi * r

print(f"Площадь круга с радиусом {r:.2f}: {area:.2f}")
print(f"Длина окружности с радиусом {r:.2f}: {circumference:.2f}")