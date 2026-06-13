n=int(input("Enter the number: "))
num=n
reversed_num=0
while n>0:
    last_digit=n%10
    reversed_num=(reversed_num*10)+last_digit
    n//=10
print("The reversed number is:",reversed_num)