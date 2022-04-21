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
			print(temp.data, "->", end=' ')
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

	# Enters after a given data
	def insertAtData(self, prevNode, data):
		
		new_node = Node(data)	
		temp = self.head

		while (temp.data != prevNode):
			temp = temp.next

			if temp is None:
				print('Previous node data does not exist.')
				return

		new_node.next = temp.next
		temp.next = new_node

	# Appends group of values to a linked list
	def insertValues(self, data_list):
		
		for data in data_list:
			self.append(data)

	# Enters at a given index
	def insertAtPosition(self, data, index):

		new_node = Node(data)

		if index<0 or index>=self.length_check():
			print('Enter a valid index.')
			return
		
		if index == 0:
			self.append(data)
			return

		count = 0
		temp = self.head

		while temp:
			if count == index - 1:
				new_node.next = temp.next
				temp.next = new_node

			temp = temp.next
			count+=1

	# Remove after a given data
	def removeAtData(self, data):
		
		if self.head and self.head.data == data:
			self.head = self.head.next
			return

		temp = self.head

		prev = None

		while temp and temp.data != data:
			prev = temp
			temp = temp.next

			if temp is None:
				print('The element is not in the list.')
				return

		prev.next = temp.next
	
	# Remove at a given index
	def removeAtIndex(self, index):

		if index<0 and index>=self.length_check():
			print('Enter a valid index.')

		if index == 0:
			self.head = self.head.next
			return
		
		count = 0
		temp = self.head

		while temp:
			if count == index-1:
				temp.next = temp.next.next
				break
		
			temp = temp.next
			count += 1

	# Reverse the linked list
	def reverseLL(self):

		curr = self.head
		prev = None

		while curr:

			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp

		self.head = prev

	# Remove duplicate data			
	def removeDuplicates(self):

		d = {} 
		temp = self.head
		prev = None

		while temp:
			if temp.data in d:
				prev.next = temp.next

			else:
				d[temp.data] = 1
				prev = temp

			temp = prev.next

if __name__ == '__main__':

	llist = LL()
	llist.append('A')
	llist.append('A')
	llist.append('B')
	llist.append('B')
	llist.append('C')
	llist.append('D')
	# llist.prepend('E')
	# llist.insertAtData('C', 'E')
	# llist.removeAtIndex(2)
	# llist.removeAtData('E')
	# llist.insertValues(['F', 'G'])
	# llist.length_check()
	# llist.reverseLL()
	# llist.removeDuplicates()
	llist.printLL()