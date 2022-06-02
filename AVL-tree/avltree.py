import sys

from requests import delete

class TreeNode(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def inset_node(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.inset_node(root.left,key)
        else: 
            root.right = self.inset_node(root.right,key)
        
        root.height = 1+max(self.getHight(root.left),self.getHight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key> root.left.key:
                return self.rightRotation(root)
            else:
                root.left = self.rightRotation(root.right)
                return self.leftRotation(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotation(root)
            else:
                root.right = self.rightRotation(root.right)
                return self.leftRotation(root)
        return root
    
    def delete_node(self,root,key):
        if  not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left,key)
        elif key> root.key:
            root.right = self.delete_node(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,temp.key)
        if root is None:
            return root

        root.height = 1+max(self.getHight(root.left),self.getHight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if self.getBalance(root.left)>=0:
                return self.rightRotation(root)
            else:
                root.left = self.leftRotation(root.left)
                return self.rightRotation(root)
        if balanceFactor < -1:
            if self.getBalance(root.right)>=0:
                return self.leftRotation(root)
            else:
                root.left = self.rightotation(root.right)
                return self.leftRotation(root)
        return root
            

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def leftRotation(self,z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1+max(self.getHight(z.left),self.getHight(z.right))
        y.height = 1+max(self.getHight(y.left),self.getHight(y.right))

        return y

    def rightRotation(self,z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left= T2

        z.height = 1+max(self.getHight(z.left),self.getHight(z.right))
        y.height = 1+max(self.getHight(y.left),self.getHight(y.right))

        return y

    def getHight(self,root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHight(root.left)-self.getHight(root.right)

    def printTree(self, currptr, indent, last):
        if currptr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent +="     "
            else:
                sys.stdout.write("L----")
                indent +="|    "
            print(currptr.key)
            self.printTree(currptr.left,indent,False)
            self.printTree(currptr.right,indent,True)

myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.inset_node(root,num)

myTree.printTree(root, "",True)

key = 13
root = myTree.delete_node(root,key)
myTree.printTree(root, "",True)

