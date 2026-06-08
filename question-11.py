a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
print("The GCD of",a, "and",b, "is: ", find_gcd(a, b))
