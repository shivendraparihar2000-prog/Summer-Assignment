def recusrsive_sum_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + recusrsive_sum_of_digits(n // 10)
num = int(input("Enter a number "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    print("The sum of the digits in", num, "is", recusrsive_sum_of_digits(num))