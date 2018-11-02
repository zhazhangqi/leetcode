def canPartitionKSubsets(nums, k):

    target, rem = divmod(sum(nums), k)
    if rem != 0 or max(nums) > target: return False
    nums.sort()
    beginIndex = len(nums) - 1
    while beginIndex >= 0 and nums[beginIndex] == target:
        beginIndex -= 1
        k -= 1
    def partition(subsets, nums, index, target):
        if index < 0 : return True
        selected = nums[index]
        for i in xrange(len(subsets)):
            if subsets[i] + selected <= target: 
                subsets[i] += selected
                if(partition(subsets, nums,index-1, target)):return True
                subsets[i] -= selected
        return False
    return partition([0] * k, nums, beginIndex, target)
a= [7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979]

# print canPartitionKSubsets(a,6)
def gcd(x,y):
    if not y: return x
    return gcd(y, x % y)
x = -20
y = 5
x2  = 20
y2 = -5
# print x/gcd(x,y) , y/gcd(x,y)
# print x2/gcd(x2,y2) , y2/gcd(x2,y2)
def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    def helper(nums, desiredTotal):
        for i in nums:
            if i >= desiredTotal: return True
            newnums = []
            for x in nums:
                if x != i:
                    newnums.append(x)
            if not helper(newnums, desiredTotal-i) : return True
        return False
    return helper([i for i in xrange(1,maxChoosableInteger+1)], desiredTotal)
print canIWin(15,100)