n=int(input("Enter the number of terms: "))
a=0
b=1
def fibo(n):
    global a,b
    if n==0:
        return a
    elif n==1:
        return b
    else:
        c=a+b
        a=b
        b=c
        return c
print("Fibonacci sequence:")
for i in range(n):
    print(fibo(i), end=" ")