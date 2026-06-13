n=int(input("Enter the number "))
num=n
sum_of_digits=0
while n>0:
    sum_of_digits+=num%10
    num//=10
    n-=1
print("The sum of digits is:",sum_of_digits)
