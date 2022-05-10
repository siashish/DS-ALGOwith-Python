
class circularqueue():

    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.front = self.rear = -1
    
    def enqueue(self,data):
        if((self.rear+1)%self.k == self.front):
            print("The Circular queue is full\n")
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.k
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front==-1):
            print("No element in the circular queue")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.queue[self.front]=None
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp = self.queue[self.front]
            self.queue[self.front]=None
            self.front = (self.front+1)% self.k
            return temp

cq = circularqueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

print(cq.queue)

cq.dequeue()
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
print(cq.queue)