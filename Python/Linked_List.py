"""
a single linked list and doubly Linked List
"""

from Nodes import Node, DoublyNode


class LinkedList:
	"""
	Class for whole list.

	Graph:
	       ob1 ----> ob2 ---> ob3 ---> Null
	       head                back
	"""
	
	def __init__(self):
		self.head = None
	
	def push(self, value):
		"""
		graph :
			Null <--- ob1 <--- ob2 <--- ob3
			        end                head

		Parameters
		----------
		value:
			the value you want to add it to the list first, at __left.
		-------
		"""
		newItem = Node(value)  # add a node
		newItem.next = self.head  # save the all list to its next
		self.head = newItem  # then save  the new variable to self head
	
	def pop(self):
		"""
		delete last item
		"""
		self.head = self.head.next
	
	def reverse(self):
		"""
		graph:


		Returns
		-------

		"""
		# self.head = ob1 --> ob2 --> ob3 --> ob4 --> Null
		temp = self.head  # temp =  ob1 --> ob2 --> ob3 --> ob4 --> Null
		x = None
		while temp is not None:
			temp1 = temp.next
			# temp =   ob1 --> ob2 --> ob3 --> ob4 --> Null
			#          temp1 = ob2 --> ob3 --> ob4 --> Null
			temp.next = x
			# temp = ob1 --> Null
			x = temp
			# x = ob1 --> Null
			temp = temp1
		# temp =  ob2 --> ob3 --> ob4 --> Null
		self.head = x
		self.print_list()
	
	def delete_first(self):
		first = self.head
		while first.next.next:
			first = first.next
		first.next = None
	
	def delete_middle(self, value):
		first = self.head
		while first.next:
			if first.next.data == value:
				temp = first.next.next
				first.next = None
				first.next = temp
			first = first.next
	
	def append(self, value):
		"""

		Parameters
		----------
		value:
		the value you want to add it to the list last, at right.
		-------
		"""
		last = self.head
		while last.next:
			last = last.next
		last.next = Node(value)
	
	def add_after(self, new_value, old_value):
		perv_node = None
		newItem = Node(new_value)
		temp = self.head
		while temp:
			if temp.data == old_value:
				perv_node = temp
				break
			if temp.next is None:
				return "Value not found"
			temp = temp.next
		newItem.next = perv_node.next
		perv_node.next = newItem
		return
	
	def print_list(self):
		"""

		Returns a string representation of the list, as a stack.
		-------
		"""
		temp = self.head
		print("[ ", end="")
		while temp:
			print(temp.data, end=" ,")
			temp = temp.next
		print("]")


class DoublyLinkedList:
	"""
	Graph:
	             ob1 ----> ob2 ---> ob3 ---> Null
	    Null<---    <----      <---    <---
	       head                back
	"""
	
	def __init__(self):
		self.head = self.back = None
	
	def append(self, value):
		new_value = DoublyNode(value)
		if self.back is None:
			self.head = self.back = new_value
			return
		self.back.next = new_value
		self.back.next.prev = self.back
		self.back = self.back.next
	
	def insertFirst(self, value):
		new_value = DoublyNode(value)
		if self.back is None:
			self.head = self.back = new_value
			return
		self.head.prev = new_value
		self.head.prev.next = self.head
		self.head = self.head.prev
	
	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()
	
	def print_reverse(self):
		temp = self.back
		while temp:
			print(temp.data, end=' ')
			temp = temp.prev
		print()
