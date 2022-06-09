def heapify(arr, n, i):
    largest = i
    l = 2 * i +1
    r = 2 * i +2

    if r<n and arr[i]<arr[l]:
        largest = l
    if r < n and arr[largest]<arr[r]:
        largest = r

    if largest !=i:
        arr[i], arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1,-1,-1):
            heapify(array,size,i)


arr = []
insert(arr,3)
insert(arr,4)
insert(arr,12)
insert(arr,2)
insert(arr,7)
insert(arr,9)
print("Hello world")

print("MAX-HEAP ARRAY: "+str(arr))