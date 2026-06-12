start=int(input("enter starting number"))
end=int(input("enter ending number"))
num_range=range(start,end+1)
for n in num_range:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)