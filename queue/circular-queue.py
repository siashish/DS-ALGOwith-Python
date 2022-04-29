
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

cq = circularqueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print(cq.queue)
print(cq.front)
print(cq.rear)