"""
BinarySearch
binary_Search_index
jump_Search
"""

import math


def binary_Search(arr, low, high, x):
	"""

	:param arr: it's the list
	:param low: start list search "it's an index"
	:param high: end list search "it's and index"
	:param x: the element
	:return: if the element in the list arr
	"""
	if high >= low:
		mid = (high + low) // 2
		# If element is present at the middle itself
		if arr[mid] == x:
			return print('YES')
		
		# If element is smaller than mid, then it can only
		# be present in __left subarray
		elif arr[mid] > x:
			return binary_Search(arr, low, mid - 1, x)
		
		# Else the element can only be present in right subarray
		else:
			return binary_Search(arr, mid + 1, high, x)
	else:
		# Element is not present in the array
		return 'NO'


def Binary_Search_Index(arr, low, high, x):
	mid = (high + low) // 2
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return binary_Search(arr, low, mid - 1, x)
	else:
		return binary_Search(arr, mid + 1, high, x)


def jump_Search(arr, x, n):
	# Finding block size to be jumped
	step = math.sqrt(n)
	
	# Finding the block where element is
	# present (if it is present)
	prev = 0
	while arr[int(min(step, n) - 1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return "NO"
	# Doing a linear search for x in
	# block beginning with prev.
	while arr[int(prev)] < x:
		prev += 1
		
		# If we reached next block or end
		# of array, element is not present.
		if prev == min(step, n):
			return "NO"
	
	# If element is found
	if arr[int(prev)] == x:
		return prev
	
	return "NO"