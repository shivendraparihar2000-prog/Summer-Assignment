n=int(input("Enter the number: "))
num=n
reversed_num=0
while n>0:
    last_digit=n%10
    reversed_num=(reversed_num*10)+last_digit
    n//=10
if num==reversed_num:
    print(num,"is a palindrome number.")
else:
    print(num,"is not a palindrome number.")
    