n=int(input("Enter the number: "))
product_of_digits=1
while n>0:
    product_of_digits*=n%10
    n//=10
print("The product of digits is:",product_of_digits)