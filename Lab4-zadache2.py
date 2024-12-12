import math 

n = int(input("натуральное число: "))

num_digits = len(str(n))

first_digit = int(str(n)[0])

print(f"Количество цифр в {n} это {num_digits}.")
print(f"Первая цифра в {n} это {first_digit}.")

