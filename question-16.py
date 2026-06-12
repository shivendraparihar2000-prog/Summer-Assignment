def armstrong_numbers(start, end):
    print("Armstrong numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        str_num = str(num)
        num_digits = len(str_num)
        digit_sum = sum(int(digit) ** num_digits for digit in str_num)
        if digit_sum == num:
            print(num, end=" ")
    print()
first_num = int(input("Enter the lower limit of the range: "))
second_num = int(input("Enter the upper limit of the range: "))
armstrong_numbers(first_num, second_num)
