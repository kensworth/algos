#Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary tree with minimal height
arr = [0,1,2,3,4,5,6,7,8,9,10]
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root) 
    def _add(self, value, node):
        if value < node.value:
            if node.left != None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else: 
            if node.right != None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    def printTree(self, node):
        if node != None:
            print node.value
            self.printTree(node.left)
            self.printTree(node.right)
bn = BinaryTree()
length = len(arr)
bn.add(arr[length / 2])
for i in range(1, length / 2):
    bn.add(arr[length / 2 + i])
    bn.add(arr[length / 2 - i])
bn.printTree(bn.root)
