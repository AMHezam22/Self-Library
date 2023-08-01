"""
ArrayQueueType: Queue implementation by array class
"""


class ArrayQueueType:
	"""
	Implementation of Queue by Array Class.
	"""
	
	def __init__(self, max_size):
		self.max_size = max_size
		self.array = [0] * max_size
		self.rear = len(self.array) - 1  # rear, back, end
		self.front = 0  # start,
		self.length = 0
	
	def isEmpty(self):
		return self.length == 0
	
	def isFull(self):
		return self.length == self.max_size
	
	def addQueue(self, element):
		if self.isFull():
			print("Queue already full")
		else:
			self.rear = (self.rear + 1) % self.max_size
			self.array[self.rear] = element
			self.length += 1
	
	def removeQueue(self):
		if self.isEmpty():
			print("Empty Queue can't be removed")
		else:
			self.front = (self.front + 1) % self.max_size
			self.length -= 1
	
	def frontQueue(self):
		if self.isEmpty():
			return "Queue is empty"
		return self.array[self.front]
	
	def rearQueue(self):
		if self.isEmpty():
			return "Queue is empty"
		return self.array[self.rear]
	
	def printQueue(self):
		if self.isEmpty():
			return "Queue is empty"
		i = self.front
		while i != self.rear:
			print(self.array[i])
			i = (i + 1) % self.max_size
		print(self.array[self.rear])
