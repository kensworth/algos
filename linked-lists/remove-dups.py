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
print 'original list:'
print_linked_list(head)
print '--'

value_set = set()
def remove_dupes(head):
	prev = None
	if head == None:
		print 'list does not exist'
		return 0
	while head != None:
		if head.data in value_set:
			prev.next_node = head.next_node
		else:
			value_set.add(head.data)
			prev = head
		head = head.next_node
remove_dupes(head)
print '--'
print 'list with no dupes:'
print_linked_list(head)
print '--'
