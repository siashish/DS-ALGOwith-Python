import sys

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
        return root

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

