def print_factors(num):
    print(f"The factors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()
number = int(input("Enter a positive integer: "))
if number <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print_factors(number)
