def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C эквивалентно {fahrenheit:.2f}°F")