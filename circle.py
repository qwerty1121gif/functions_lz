import math

r = float(input("Введите радиус круга: "))

AreaOfCircle = math.pi * r**2
circlen = 2 * math.pi * r

print(f"Площадь круга с радиусом {r:.2f}: {AreaOfCircle:.2f}")
print(f"Длина окружности с радиусом {r:.2f}: {circlen:.2f}")