"""
single node for Linkedlist. which has a next attribute only.
and doubly node for doubly linkedlist which has a next attribute and previous attribute.
"""


class Node:
	"""
	Class for each node in a Linked List, LinkedQueue.

	Graph:
		|   Node    |
		 data , next ---> None
	"""
	
	def __init__(self, data):
		self.data = data
		self.next = None


class DoublyNode:
	"""
	Graph:
		            |       Node        |
		   None <--- prev , data , next ---> None
	"""
	
	def __init__(self, value):
		self.data = value
		self.next = self.prev = None
