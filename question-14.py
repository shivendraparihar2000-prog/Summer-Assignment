n=int(input("Enter the number of terms: "))
a=0
b=1
def fibo(n):
    global a,b
    if n<=1:
        return a
    elif n==2:
        return b
    else:
        for i in range(3, n+1):
            c=a+b
            a=b
            b=c
    return b
result=fibo(n)
print("The nth term of the Fibonacci sequence is:", result)