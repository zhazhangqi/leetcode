sol = [0]
def cumsum(nums, idx):
	if idx == len(nums): return sol
	sol[0] += nums[idx]
	cumsum(nums,idx+1)

cumsum([1,2,3,4,5], 0)
print sol[0]
