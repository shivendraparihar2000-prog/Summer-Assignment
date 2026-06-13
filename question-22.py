def binary_to_decimal(binary_str):
    decimal_sum = 0
    power = 0
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_sum += 2 ** power
        elif digit != '0':
            return None  
        power += 1  
    return decimal_sum
binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
if decimal_output is None:
    print("Invalid input! Please enter a valid binary number containing only 0s and 1s.")
else:
    print("The decimal equivalent is:", decimal_output)
