def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
num = int(input("Enter number  "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("The factorial of ",num, "is", recursive_factorial(num))