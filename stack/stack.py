# stack implementation in python

# Create a stack
from turtle import st


def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print("pushed item ",item)

def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

def peak(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack[-1]


stack = create_stack()
print(peak(stack))
push(stack,21)
push(stack,40)
push(stack,34)
print(stack)
pop(stack)
pop(stack)
push(stack,78)
print(stack)
print(peak(stack))
