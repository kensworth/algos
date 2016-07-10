#Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary tree with minimal height
arr = [0,1,2,3,4,5,6,7,8,9,10]
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sortedArrayToMinHeightBST(arr, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    node = Node(arr[mid])
    node.left = sortedArrayToMinHeightBST(arr, start, mid - 1)
    node.right = sortedArrayToMinHeightBST(arr, mid + 1, end)
    return node

def preOrderPrint(node):
    if node == None:
        return None
    print node.value
    preOrderPrint(node.left)
    preOrderPrint(node.right)

node = sortedArrayToMinHeightBST(arr, 0, len(arr) - 1)
preOrderPrint(node)
