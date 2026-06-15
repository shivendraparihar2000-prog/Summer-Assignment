def recersive_reverse_number(n):
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (len(str(n)) - 1)) + recersive_reverse_number(n // 10)
num = int(input("Enter a number "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    print("The reverse of", num, "is", recersive_reverse_number(num))