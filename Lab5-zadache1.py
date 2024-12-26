import math

product = 1
for number in range(13, 100, 13):  
    if 10 <= number < 100 and number % 2 != 0:
        product *= number

print("произведение дв