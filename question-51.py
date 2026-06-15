array=[10,20,30,40,50]
largest=array[0]
smallest=array[0]
for i in array:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("The largest number in the array is:",largest)
print("The smallest number in the array is:",smallest)