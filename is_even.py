def is_even(number):
    if number % 2 == 0:
        print(f"Число {number} четное")
    else:
        print(f"Число {number} нечетное")

try:
    num = int(input("Введите целое число: "))
    is_even(num)
except ValueError:
    print("Значение введено неверно")