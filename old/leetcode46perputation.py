class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        if len(nums) == 1: return [nums]
        q = [[nums[0]]]
        for i in xrange(1, len(nums)):
            size = len(q)
            print 'q is:', q
            for j in xrange(size):
                temp = q.pop(0)
                for k in xrange(len(temp)+1):
                    q.append(temp[:k] + [nums[i]] + temp[k:])
                    # q.append(temp + [nums[i]])
        return q
a = [1,2,3]
b =Solution()
print b.permute(a)
# k = 3
# print a[:k] + ['x'] + a[k:]