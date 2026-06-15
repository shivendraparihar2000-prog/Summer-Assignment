def count_set_bits(num):
    if num < 0:
        return "Please enter a non-negative integer."
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num = num // 2
    return count
number = int(input("Enter a positive integer: "))
result = count_set_bits(number)
print("Number of set bits in the binary form:",result)
