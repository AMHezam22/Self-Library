"""
normal queue implemented as a linked list.
"""
from Nodes import Node


class Queue:
	"""
	Class for whole list.
	FIFO:
		First in First Out
		Parameters
	Graph:
		   ob1 ----> ob2 ---> ob3 ---> Null
		   head               tail
		   front                end
	"""
	
	def __init__(self):
		self.front = self.rear = None
	
	def enQueue(self, value):
		"""
		Graph:
		   ob1 ----> ob2 ---> ob3 ---> Null
		   head               tail
		   front                end
		Becomes:
		   ob1 ---> ob2 ----> ob3 --------> ob4 ---> Null
		   head                rear -->    rear
		----------
		value:
			the value you want to add it to the list first, at right.
		-------
		"""
		
		new_item = Node(value)
		if self.rear is None:
			self.front = self.rear = new_item
			return
		self.rear.next = new_item  # save the all list to its next
		self.rear = new_item
	
	def deQueue(self):
		"""
		Graph:

		Becomes:
		   ob1 ----> ob2 ---> ob3 ---> Null
		   head                rear
		To:
		   ob1 ----> ob2 ---> ob3 --->Null
		             head      rear
		delete last item
		"""
		self.front = self.front.next
	
	def getFront(self):
		return self.front
	
	def getRear(self):
		return self.rear
	
	def print_list(self):
		"""

		Returns a string representation of the list, as a stack.
		-------
		"""
		temp = self.front
		print("[ ", end="")
		while temp:
			print(temp.data, end=" ,")
			temp = temp.next
		print("]")
