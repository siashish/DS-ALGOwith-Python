import array as arr

# Initilazion 
array1 = arr.array('i',[10,20,30,40,50])


# Traversing
for idx, x in enumerate (array1):
    print(idx,x)

# Accessing element
print()
print("Accessing element")
print(array1[2])
print(array1[-1])
print(array1[-5])
print(array1[-len(array1)])

# length of array
print("length of array")
print(len(array1))

# insert element in array
print("insert element in array")
print(array1)
array1.insert(4,34)
array1.insert(5,67)
print(array1)

array1.append(9)
print(array1)

# deletion of element
print("deletion of element")
print(array1)
array1.remove(30)
print(array1)
array1.pop(2)
array1.pop()
print(array1)

# Update in array
print("Update in array")
print(array1)
array1[2]=90
print(array1)
