def decimal_to_binary(num):
    if num == 0:
        return "0"
    binary_string = ""
    while num > 0:
        remainder = num % 2
        binary_string = str(remainder) + binary_string  
        num = num // 2  
    return binary_string
decimal_num = int(input("Enter a positive decimal number: "))
if decimal_num < 0:
    print("Please enter a non-negative integer.")
else:
    binary_num = decimal_to_binary(decimal_num)
    print("The binary equivalent is:", binary_num)
