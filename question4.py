n=int(input("enter n"))
digits=0
while n>0:
    n=n//10
    digits=digits+1
print("Number of digits =",digits)
