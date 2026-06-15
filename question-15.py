num = int(input("Enter a number: "))
order = len(str(num))
sum_val = 0
t = num
while t > 0:
    digit = t % 10
    sum_val += digit ** order
    t //= 10
if num == sum_val:
    print(num," is an Armstrong number.")
else:
    print(num," is not an Armstrong number.")
