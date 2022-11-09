"""
bubble_Sort
section_Sort
merge_Sort
insertion_Sort
head_Sort
"""


def bubble_Sort(arr):
	"""
	Time complexity: O(n^2)
	space complexity: O(1)
	"""
	flag = True  # in case the arr is already sorted.
	# Traverse through all array elements
	for i in range(len(arr)):
		# Last i elements are already in place
		for j in range(0, arr - i - 1):
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				flag = False
	if flag:
		return


def insertion_Sort(arr):
	"""
	Tim complexity: O(n^2)
	space complexity: O(1)
	it could be good for linked lists, because you don't have to shift the elements. you could just insert.
	"""
	for i in range(1, len(arr)):
		j = i
		while j > 0:
			if arr[j] < arr[j - 1]:
				arr[j], arr[j - 1] = arr[j - 1], arr[j]
			j -= 1
	return arr


def section_Sort(arr):
	"""
	time complexity: O(n^2).
	space complexity: O(1)
	"""
	for x in range(len(arr)):
		mini = x
		for i in range(x + 1, len(arr)):
			if arr[i] < arr[mini]:
				mini = i
		arr[x], arr[mini] = arr[mini], arr[x]
	return arr


def addition(arr1, arr2):
	"""
	for merge_Sort
	:param arr1:
	:param arr2:
	:return: collect two arrays together
	"""
	arr = []
	i = j = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			arr.append(arr1[i])
			i += 1
		else:
			arr.append(arr2[j])
			j += 1
	while i < len(arr1):
		arr.append(arr1[i])
		i += 1
	while j < len(arr2):
		arr.append(arr2[j])
		j += 1
	return arr


def merge_Sort(arr):
	"""
	Time complexity: O(n log n)
	space complexity: O(n)
	"""
	if len(arr) == 1:
		return arr
	mid = len(arr) // 2
	arr1, arr2 = arr[:mid], arr[mid:]
	return addition(merge_Sort(arr1), merge_Sort(arr2))


def heapify(arr, n, i):
	"""
	 used in heap sort
	:param arr:
	:param n: array length
	:param i:
	:return:
	"""
	largest = i  # Initialize largest as root
	left = 2 * i + 1  # __left = 2*i + 1
	r = 2 * i + 2  # right = 2*i + 2
	
	# See if __left child of root exists and is
	# greater than root
	if left < n and arr[i] < arr[left]:
		largest = left
	
	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r
	
	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # swap
		
		# Heapify the root.
		heapify(arr, n, largest)


def heap_Sort(arr):
	"""
	The main function to sort an array of given size
	:param arr:
	:return:
	"""
	n = len(arr)
	
	# Build a max heap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)
	# One by one extract elements
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]  # swap
		heapify(arr, i, 0)
