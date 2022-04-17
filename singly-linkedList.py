class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LL:
	def __init__(self):
		self.head = None

	# Node count
	def length_check(self):
		temp = self.head
		counter = 0

		if temp is None:
			print('The Linked List is empty')
			return
		
		while temp:
			counter += 1
			temp = temp.next
		
		print(counter)

	# Prints content of the list
	def printLL(self):
		temp = self.head
		while temp:
			print(temp.data, end='\n')
			temp = temp.next
	
	# Enters at the end
	def append(self, data):
		new_node = Node(data)
		
		if self.head is None:
			self.head = new_node
			return
		
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = new_node

	# Enters in the beginning
	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	# Enters at a given position
	def addAtPosition(self, prevNode, data):
		
		new_node = Node(data)		
		temp = self.head

		while (temp.data != prevNode):
			temp = temp.next

			if temp is None:
				print('Previous node data does not exist.')
				return

		new_node.next = temp.next
		temp.next = new_node	

llist = LL()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.prepend('E')
llist.addAtPosition('C', 'E')
# llist.length_check()
llist.printLL()