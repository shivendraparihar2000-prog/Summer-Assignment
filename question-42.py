a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter the third number: "))
def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(maximum(a,b,c))