def is_perfect_number(num):
    if num <= 0:
        return False
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num
number = int(input("Enter a number to check: "))
if is_perfect_number(number):
    print(number, " is a Perfect Number.")
else:
    print(number, " is NOT a Perfect Number.")
