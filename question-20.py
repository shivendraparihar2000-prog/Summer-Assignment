def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    result = 1
    if exponent > 0:
        for _ in range(exponent):
            result *= base
    else:
        for _ in range(-exponent):
            result *= base
        result = 1 / result
    return result
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
output = calculate_power(x, n)
print(x, "{raised to the power of is",output)
