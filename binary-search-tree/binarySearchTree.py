from http import server
from readline import insert_text
from tkinter import NO


class Node:
    def __init__(self,key):
        self.Key = key
        self.left = None
        self.right = None

def insert(node,key):
        if node is None:
            return Node(key)
        
        if key < node.Key:
            node.left = insert(node.left,key)
        else: 
            node.right = insert(node.right,key)

        return node

def inorder(root):
    if root is not None:
        # traversr left
        inorder(root.left)

        # print root
        print(str(root.Key)+" -> ",end=' ')

        # traverse right
        inorder(root.right)

def search(node,key):
    if node is None:
        return None
    if key == node.Key:
        return node.Key
    if key < node.Key:
        return search(node.left,key)
    if key > node.Key:
        return search(node.right,key)

def minValue(node):
    current = node

    while(current.left is not None):
        current = current.left
    return current

def delete(root,key):
    if root is None:
        return root
    if key < root.Key:
        root.left = delete(root.left,key)
    if key > root.Key:
        root.right = delete(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValue(root.right)
        root.Key = temp.Key
        root.right = delete(root.right,temp.Key)

    return root
    

root = None
root = insert(root,10)
root = insert(root,8)
root = insert(root,11)
root = insert(root,6)
root = insert(root,7)

print("Inorder traversal ",end=' ')
inorder(root)
print()

var = search(root,11)

if var!= None:
    print("found the element")
else:
    print("not found")

root = delete(root,10)

print("Inorder traversal ",end=' ')
inorder(root)

