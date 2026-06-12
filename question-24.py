def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    n = abs(exponent)
    result = 1
    current_product = base
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2
    if exponent < 0:
        return 1 / result
    return result
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
output = calculate_power(x, n)
print(x," raised to the power of",n," is: ",output)