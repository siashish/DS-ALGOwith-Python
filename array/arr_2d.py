# Initilazion 
arr2d = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# accessing value
print(arr2d[2])
print(arr2d[1][3])
print(arr2d)

# Traversing
for i in arr2d:
    for j in i:
        print(j,end=" ")
    print()

# insert element in array
print(arr2d)
arr2d.insert(2,[4,7,5])
print(arr2d)
arr2d[2].append(0)
arr2d[2].insert(2,9)
print(arr2d)

# deletion of element
del(arr2d[2][3])
print(arr2d)
arr2d[2].remove(9)
print(arr2d)
arr2d[3].pop(2)
print(arr2d)

# update the array
arr2d[0][0]=34
print(arr2d)
arr2d[1]=[12,34,34,23]
print(arr2d)


# search
a = 7
for idx,i in enumerate( arr2d):
    for jdx, j in  enumerate( i):
        if j==a:
            print(idx,jdx)

