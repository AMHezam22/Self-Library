"""
Binary tree implementation. has :
	- insert: adding a value into the tree.
	- delete: delete a node by replacing the predecessor or successor.
	- balance: balance the tree
	- avlTree_Editing: Tree arrangement by AVLTree
	- ll_Rotation: for AVLTree
	- successor: return the successor node.
	- predecessor: return the predecessor node.
	- min_tree: minimum value.
	- max_tree: maximum value.
	- display: display the tree.
	- search
	- inOrderTraversal
	- preOrderTraversal
	- postOrderTraversal.
	
"""


class BinaryTree:
	
	def __init__(self, node, left=None, right=None):
		self.__left = left
		self.__right = right
		self.__prev = None  # I added it to use successor and predecessor methods.
		self.__node = node
		self.__balance = None  # I added it to use AVLTree insertion method.
	
	def insert(self, value):
		"""
		:param value: the value to insert into the
		:type value: int
		:returns: insert it to binary tree.
		:rtype: int
		"""
		if value <= self.__node:
			if self.__left is None:
				self.__left = BinaryTree(value)
				self.__left.__prev = self
			else:
				self.__left.insert(value)
		if value > self.__node:
			if self.__right is None:
				self.__right = BinaryTree(value)
				self.__right.__prev = self
			else:
				self.__right.insert(value)
	
	def __clear(self):
		if self.__prev.__node < self.__node:
			self.__prev.__right = None
		else:
			self.__prev.__left = None
		self.__prev = None
		self.__right = None
		self.__left = None
	
	def delete(self, value):
		# the problem is the attribute prev, in case you delete a node, and you didn't change the prev attribute to the
		# new node
		node = self.__search(value)
		new_node = node.__successor()
		if new_node:
			if node.__left.__node <= new_node.__node < node.__right.__node:
				new_node.__prev.__left = new_node.__right
		else:
			new_node = node.__predecessor()
			if new_node:
				if new_node and node.__left.__node <= new_node.__node < node.__right.__node:
					new_node.__prev.__right = new_node.__left
			else:
				node = None
				return
			if node.__left:
				node.__left.__prev = node.__prev
			else:
				node.__right__prev = node.__prev
			if node.__prev.__node <= node.__node:
				node.__prev.__right = node.__right
			else:
				node.__prev.__left = node.__left
				return
		if new_node is None:
			node = None
			return
		new_node.__clear()
		new_node.__right = node.__right
		new_node.__left = node.__left
		new_node.__prev = node.__prev
		if node.__prev.__node >= node.__node:
			node.__prev.__left = new_node
		else:
			node.__prev.__right = new_node
		node.__left = None
		node.__right = None
		del node
	
	def balance(self):
		b = 0
		temp = self.__left
		while temp:
			b += 1
			if temp.__left:
				temp.__left.balance()
			temp = self.__left
		temp = self.__right
		while temp:
			b += 1
			if temp.__right:
				temp.__right.balance()
			temp = self.__right
		self.__balance = b
	
	def avlTree_Editing(self, value):
		pass
	
	def ll_Rotation(self):
		temp = self.__left.__right
		self.__left.__right = self
		# self = self.__left.__right
		self.__right.__left = temp
	
	def __predecessor(self):
		"""
		this method for delete method, for more information about how to find the predecessor of a node
		  go to predecessor method.
		"""
		node = self
		if node:
			if node.__left:  # if node has a right child
				return node.__left.__max_Tree()
			else:  # if node doesn't have a right child
				if node.__node > node.__prev.__node:
					return node.__prev
				else:
					temp = node.__prev
					while temp.__prev:
						if temp.__node > temp.__prev.__node:
							return temp.__prev
						temp = temp.__prev
					return False
		else:
			return False
	
	def __successor(self):
		"""
		this method use it for delete method. for more details how find successor of node go successor method.
		"""
		node = self
		if node:
			if node.__right:  # if node has a right child
				return node.__right.__min_Tree()
			else:  # if node doesn't have a right child
				if node.__node <= node.__prev.__node:
					return node.__prev
				else:
					temp = node.__prev
					while temp.__prev:
						if temp.__node <= temp.__prev.__node:
							return temp.__prev
						temp = temp.__prev
					return False
		else:
			return False
	
	def successor(self, node):
		"""
		there are 3 ways to find the successor of a node depends on what if the node it's the right or __left child of its
		parent.

		- **if the node has a right child** ::

			  the successor is the minimum of this child.

		- **if the node doesn't have a right child and** ::

			- the node is the right child of its parent
				  the successor is the first right parent or None will return -1.
				                _____________
				                |           |
				                | successor |
				                |           |
				                -------------
				               /
				  _____________
				  |           |
				  |   parent  |
				  |           |
				  -------------
				               \\
				                _____________
				                |           |
				                |   node    |
				                |           |
				                -------------

			- the node is the __left child of its parent.
				  the successor is its parent.
				                  _____________
				                  |           |
				                  | successor |
				                  |           |
				                  -------------
				                /
				               /
				  _____________
				  |           |
				  |   node    |
				  |           |
				  -------------


		.. note::  the method will return -2 in case the node is not inside the tree,
				   and -1 in case there aren't successor

		:param node: The node to find its successor.
		:type node: int
		:return: the successor of node
		:rtype: int
		"""
		node = self.__search(node)
		if node:
			if node.__right:  # if node has a right child
				return node.__right.min_Tree()
			else:  # if node doesn't have a right child
				if node.__node <= node.__prev.__node:
					return node.__prev.__node
				else:
					temp = node.__prev
					while temp.__prev:
						if temp.__node <= temp.__prev.__node:
							return temp.__prev.__node
						temp = temp.__prev
					return -1
		else:
			return -2
	
	def predecessor(self, node):
		"""
		there are 3 ways to find the predecessor of a node, depends on what if the node it's the __left or right child
		of its parent.

		- **if the node has a __left child** ::

			  the successor is the maximum of this child.

		- **if the node doesn't have a __left child and** ::

			- the node is the __left child of its parent
				  the successor is the first right parent or NULL.
				  _____________
				  |           |
				  |predecessor|
				  |           |
				  -------------
				              \\
				               _____________
				               |           |
				               |   parent  |
				               |           |
				               -------------
				             /
				  _____________
				  |           |
				  |   node    |
				  |           |
				  -------------

			- the node is the right child of its parent.
				  the successor is its parent.
				  _____________
				  |           |
				  |predecessor|
				  |           |
				  -------------
				              \\
				              _____________
				              |           |
				              |   node    |
				              |           |
				              -------------

		.. note::
			  the method wil return -2 if the node isn't inside the tree, and -1 if there isn't predecessor to the node.
		:param node: The node to find its predecessor.
		:type node: int
		:return: the predecessor of node
		:rtype: int
		"""
		node = self.__search(node)
		if node:
			if node.__left:  # if node has a right child
				return node.__left.max_Tree()
			else:  # if node doesn't have a right child
				if node.__node > node.__prev.__node:
					return node.__prev.__node
				else:
					temp = node.__prev
					while temp.__prev:
						if temp.__node > temp.__prev.__node:
							return temp.__prev.__node
						temp = temp.__prev
					return -1
		else:
			return -2
	
	def min_Tree(self):
		"""
		:return: the minimum node of the tree
		:rtype: int
		"""
		temp = self
		while temp.__left:
			temp = temp.__left
		return temp.__node
	
	def __min_Tree(self):
		"""
		:return: the minimum node of the tree
		:rtype: int
		"""
		temp = self
		while temp.__left:
			temp = temp.__left
		return temp
	
	def max_Tree(self):
		"""

		:return: the maximum node of the tree
		:rtype: int
		"""
		temp = self
		while temp.__right:
			temp = temp.__right
		return temp.__node
	
	def __max_Tree(self):
		"""

		:return: the maximum node of the tree
		:rtype: int
		"""
		temp = self
		while temp.__right:
			temp = temp.__right
		return temp
	
	def display(self):
		"""
		:returns: print a string representation of the tree.
		:rtype: str
		"""
		lines, *_ = self.__display_aux()
		for line in lines:
			print(line)
	
	def __display_aux(self):
		# No child.
		if self.__right is None and self.__left is None:
			line = '%s' % self.__node
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle
		
		# Only __left child.
		if self.__right is None:
			lines, n, p, x = self.__left.__display_aux()
			s = '%s' % self.__node
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
		
		# Only right child.
		if self.__left is None:
			lines, n, p, x = self.__right.__display_aux()
			s = '%s' % self.__node
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
		
		# Two children.
		left, n, p, x = self.__left.__display_aux()
		right, m, q, y = self.__right.__display_aux()
		s = '%s' % self.__node
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2
	
	def inOrderTraversal(self):
		"""
		this method to print the tree in order traversal.

		.. note::
		     modified to can use it to expression binary tree.
		:return: print representation using Left root right order
		:rtype: None
		"""
		if self.__left:
			try:
				self.__left.inOrderTraversal()
			except AttributeError:
				print(self.__left, end=' ')
		print(self.__node, end=" ")
		if self.__right:
			try:
				self.__right.inOrderTraversal()
			except AttributeError:
				print(self.__right, end=' ')
	
	def preOrderTraversal(self):
		"""
		:return: print representation using root Left right order
		:rtype: None
		"""
		print(self.__node, end=" ")
		if self.__left:
			self.__left.preOrderTraversal()
		if self.__right:
			self.__right.preOrderTraversal()
	
	def __search(self, __value):
		"""

		:return: BinaryTree node if found
		:rtype: BinaryTree
		"""
		if self.__node:
			if __value < self.__node:
				if self.__left is None:
					return False
				else:
					return self.__left.__search(__value)
			elif __value > self.__node:
				if self.__right is None:
					return False
				else:
					return self.__right.__search(__value)
			else:
				return self
		else:
			return False
	
	@staticmethod
	def __check(i, sign):
		operators_order = {'*': 2, '/': 2, '^': 3, '+': 1, '-': 1}
		try:
			return operators_order[i] <= operators_order[sign]
		except KeyError:
			return False
	
	def infix2ExpressionTree(self, expression: str):
		"""
		:param expression: mathematical expression to convert it to binary tree.
		:return: call inOrderTraversal to print the tree.
		"""
		expression = expression.split()
		signs = []
		nodes = []
		for i in expression:
			if i.isalnum():
				nodes.append(i)
			else:
				while signs and len(nodes) > 1 and self.__check(i, signs[-1]):
					if i == '^' == signs[-1]:
						break
					right, node, left = nodes.pop(), signs.pop(), nodes.pop()
					nodes.append(BinaryTree(self.__node, self.__left, self.__right))
				signs.append(i)
		right, node, left = nodes.pop(), signs.pop(), nodes.pop()
		nodes.append(BinaryTree(self.__node, self.__left, self.__right))
		nodes[-1].inOrderTraversal()
	
	def postOrderTraversal(self):
		"""
		this method to print the tree using post order traversal.

		:return: print representation using Left right root order
		:rtype: None
		"""
		if self.__left:
			self.__left.postOrderTraversal()
		if self.__right:
			self.__right.postOrderTraversal()
		print(self.__node, end=" ")
	
	def search(self, value):
		"""
		return False if not found, else return True.
		:param value: The node you want to find
		:rtype: boolean
		"""
		if self.__node:
			if value <= self.__node:
				if self.__left is None:
					return False
				else:
					return self.__left.search(value)
			elif value > self.__node:
				if self.__right is None:
					return False
				else:
					return self.__right.search(value)
			else:
				return True
		else:
			return False