class BinarySearch(object):
	"""docstring for BinarySearch
	第一处是right的初始化，可以写成 nums.size() 或者 nums.size() - 1,第二处是left和right的关系，可以写成 left < right 或者 left <= right, 第三处是最后right的赋值，可以写成 right = mid 或者 right = mid - 1, 但是这些不同的写法并不能随机的组合，像博主的那种写法，若right初始化为了nums.size()，那么就必须用left < right，而最后的right的赋值，用哪个都可以，博主偷懒就不写-1了。但是如果我们right初始化为 nums.size() - 1，那么就必须用 left <= right，并且right的赋值要写成 right = mid - 1，不然就会出错。所以博主的建议是选择一套自己喜欢的写法，并且记住，实在不行就带简单的例子来一步一步执行，确定正确的写法也行。
	"""
	def binary(self, nums, target):
		l = 0
		r = len(nums)
		while l < r:
			m = (r+l)/2
			if nums[m] == target: return m
			if nums[m] < target:
				l = m + 1
			else:
				r = m
	'''第二类： 查找第一个不小于目标值的数，可变形为查找第一个小于目标值的数,这是比较常见的一类，因为我们要查找的目标值不一定会在数组中出现，也有可能是跟目标值相等的数在数组中并不唯一，而是有多个，那么这种情况下nums[mid] == target这条判断语句就没有必要存在。比如在数组[2, 4, 5, 6, 9]中查找数字3，就会返回数字4的位置；在数组[0, 1, 1, 1, 1]中查找数字1，就会返回第一个数字1的位置。我们可以使用如下代码：

	这一类可以轻松的变形为查找第一个小于目标值的数，怎么变呢。我们已经找到了第一个不小于目标值的数，那么再往前退一位，返回right - 1，就是第一个小于目标值的数。'''
	def binaryFirstNoLess(self, nums, target):
		l = 0
		r = len(nums)
		while l < r:
			m = (r+l)/2
			if nums[m] < target:
				l = m + 1
			else:
				r = m				
		return r
	'''第三类： 查找第一个大于目标值的数，可变形为查找最后一个不小于目标值的数, 这一类也比较常见，尤其是查找第一个大于目标值的数，在C++的STL也有专门的函数upper_bound，这里跟上面的那种情况的写法上很相似，只需要添加一个等号，将之前的 nums[mid] < target 变成 nums[mid] <= target，就这一个小小的变化，其实直接就改变了搜索的方向，使得在数组中有很多跟目标值相同的数字存在的情况下，返回最后一个相同的数字的下一个位置。比如在数组[2, 4, 5, 6, 9]中查找数字3，还是返回数字4的位置，这跟上面那查找方式返回的结果相同，因为数字4在此数组中既是第一个不小于目标值3的数，也是第一个大于目标值3的数，所以make sense；在数组[0, 1, 1, 1, 1]中查找数字1，就会返回坐标5，通过对比返回的坐标和数组的长度，我们就知道是否存在这样一个大于目标值的数。参见下面的代码：

	这一类可以轻松的变形为查找最后一个不小于目标值的数，怎么变呢。我们已经找到了第一个大于目标值的数，那么再往前退一位，返回right - 1，就是最后一个不小于目标值的数。比如在数组[0, 1, 1, 1, 1]中查找数字1，就会返回最后一个数字1的位置4，这在有些情况下是需要这么做的。'''	
	def binaryFirstLarger(self, nums, target):
		l = 0
		r = len(nums)
		while l < r:
			m = (r+l)/2
			if nums[m] <= target:
				l = m + 1
			else:
				r = m				
		return r
nums = [1,2,3,4,5,6,7,8,9]
a = BinarySearch()
print a.binaryFirstNoLess(nums, 3)
print a.binaryFirstLarger(nums, 3)
print a.binary(nums, 3)
