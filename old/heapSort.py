class Sort(object):

	def heaplify(self, arry, n, i):
		l = i * 2 + 1
		r = i * 2 + 2
		largest = i
		if l < n and arry[largest] < arry[l]:
			largest = l
		if r < n and arry[largest] < arry[r]:
			largest = r
		if largest != i:
			arry[i], arry[largest] = arry[largest], arry[i]
			self.heaplify(arry, n, largest)

	def heapSort(self, arry):
	  	n = len(arry)
	  	for i in xrange(n, -1, -1):
	  		self.heaplify(arry, n, i)
	  	for i in xrange(n-1, 0, -1):
	  		arry[i], arry[0] = arry[0], arry[i]
	  		self.heaplify(arry, i, 0)
	
	def partition(self, nums, low, high):
		i = low - 1
		for j in xrange(low, high):
			if nums[j] <= nums[high]:
				i += 1
				nums[i], nums[j] = nums[j], nums[i]
		nums[i+1], nums[high] = nums[high], nums[i+1]
		return i + 1
	def quickSort(self, nums, low, high):
		if low < high:
			pi = self.partition(nums, low, high)
			self.quickSort(nums, low, pi - 1)
			self.quickSort(nums, pi + 1, high)

a = Sort()
arry = [4,5,32,3,4,8,9,65,7]
a.quickSort(arry, 0, len(arry)-1)
print arry