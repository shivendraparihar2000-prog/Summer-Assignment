array=[30,20,10,50,40]
count_odd=0
count_even=0
for i in array:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("The number of odd numbers in the array is:",count_odd)
print("The number of even numbers in the array is:",count_even)