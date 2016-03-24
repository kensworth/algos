#write an algorithm to find the kth to last node in a singly linked list. Ex. kthToLast(5) would return the value of the 5th to last node.

def kthToLast(head, k):
    #using extra compute time by first running through and counting the nodes rather than using extra memory by storing the last k elements, in case k is very large. Could be done either way though
    if k < 1:
        return None
    count = 0
    end = False
    iterable = head
    while not end: 
        count += 1
        if iterable.next_node != None:
            iterable = iterable.next_node
        else:
            end = True
    target = count - k + 1 
    for i in range(1, target):
        head = head.next_node
    return head.data

#remove duplicates from a an unsorted linked list
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

six = Node(0, None)
five = Node(1, six)
four = Node(2, five)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)
head = Node(0, one)

def print_linked_list(head):
	if head != None:
		print head.data
	else:
		print 'list does not exist'
	while head.next_node != None:
		head = head.next_node
		print head.data
print '--'
print_linked_list(head)
print '--'

print '2nd to last'
print(kthToLast(head, 2))
