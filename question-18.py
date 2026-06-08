import math

def is_strong_number(num):
    if num <= 0:
        return False
    temp = num
    factorial_sum = 0
    while temp > 0:
        digit = temp % 10       
        factorial_sum += math.factorial(digit)  
        temp //= 10
    return factorial_sum == num
number = int(input("Enter a number to check: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is NOT a Strong Number.")
