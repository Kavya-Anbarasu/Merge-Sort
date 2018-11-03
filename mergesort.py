def merge_sort(array):
	left = []
	right = []

	if len(array) <= 1:
		return array

	for x in range(0 , len(array)):
		if x < len(array) / 2:
			left.append(array[x])
		else:
			right.append(array[x])

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left , right)

def merge(left , right):
	result = []

	while len(left) >= 1 and len(right) >= 1 :
		if left[0] <= right[0]:
			result.append(left[0])
			left.remove(left[0])
		else:
			result.append(right[0])
			right.remove(right[0])
		
	while len(left) >= 1:
		result.append(left[0])
		left.remove(left[0])
	while len(right) >= 1:
		result.append(right[0])
		right.remove(right[0])
	return result

list = [9 , 32 , 1 , 27 , 13 , 4 , 3 , 16 , 20]
print(merge_sort(list))
