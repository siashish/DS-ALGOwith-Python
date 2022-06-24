def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2,n//2):
        if n%i==0:
            return 0
    
    return 1

def getPrime(n):
    if n%2==0:
        n = n+1
    while not checkPrime(n):
        n +=2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key%capacity

hashTable = [[],]*10

def insert(key,data):
    index = hashFunction(key)
    hashTable[index] = [key,data]

def remove(key):
    index = hashFunction(key)
    hashTable[index]=0


insert(123,"Ashish")
insert(432,"Manish")
insert(213,"Rutvik")
insert(654,"Bikash")

print(hashTable)

remove(123)

print(hashTable)

