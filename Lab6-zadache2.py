import math 

def compute_a_n(n):
    a = 1
    for k in range(2, n + 1):
        a = a / k + k
    return a

n = int(input("natural number n: "))
result = compute_a_n(n)
print(f"a_{n} = {result}")