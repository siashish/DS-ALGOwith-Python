# Enqueue
# Dequeue
# IsEmpty
# IsFull
# Peek

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)

    def display(self):
        print(self.queue)

    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(34)
q.enqueue(75)
q.enqueue(78)
q.enqueue(56)
q.display()
q.dequeue()
q.enqueue(99)
q.dequeue()
q.enqueue(100)
q.enqueue(377)
q.dequeue()
q.display()
print(q.size())
