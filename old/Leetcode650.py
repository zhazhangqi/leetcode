# # class Solution(object):
# # 	def miniSteps(self, n):
# # 		res = 0
# # 		for x in xrange(2,n+1):
# # 			while (n % x == 0):
# # 				res += x
# # 				n = n/x
# # 		return res

# # s = Solution()
# # print s.miniSteps(997) 


# # 		
# # nums = [0,0,1,2,0,3,4,0,0,0,0,0,1]
# # # if 5<3 and a[12]< 1: print a[12]

# # # b = set(a)
# # # print b[5]
# # count = 0
# # for x in range(len(nums)):
# # 	if nums[x] == 0:
# # 		count += 1
# # 		del nums[x]
# # 		print nums
	
# # for x in range(count):
# # 	nums.append(0)
# # print nums
# # A ='abcd'
# # B ='dabcda'
# # a = len(A)
# # b = len(B)
# # n = 2 * b / a + 1
# # print n
# # C=A+A
# # print C.count(B)

# # Definition for a binary tree node.
# # class TreeNode(object):
# # 	def __init__(self, x):
# # 		self.val = x
# # 		self.left = None
# # 		self.right = None

# # t1 = TreeNode(1)
# # t2 = TreeNode(2)
# # t3 = TreeNode(3)
# # t4 = TreeNode(4)
# # t5 = TreeNode(5)
# # t6 = TreeNode(6)
# # t7 = TreeNode(7)
# # t8 = TreeNode(8)
# # t1.left = t2
# # t1.right = t3
# # t2.right = t4
# # t3.left = t5
# # t3.right = t6
# # t4.left = t7
# # t5.right = t8

# # class Solution(object):
# # 	def tree2str(self, t):
# # 		if t == None: return ''
# # 		if t.left == None and t.right == None: return str(t.val)
# # 		if t.right == None: return str(t.val) + '(' + self.tree2str(t.left) + ')'
# # 		else: return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')' 		

# # s = Solution()
# # print s.tree2str(t1)

# # a='a'
# # b='bcab'
# # if a in b : 
# # 	print b.index(a)


# # a = 'abc ghj fds'
# # def reversWord(a):
# # 	return a[::-1]
# # c = ''
# # j = 0
# # for i in range(len(a)):
# # 	if a[i]==' ':
# # 		c = c + reversWord(a[j:i]) + ' '
# # 		j = i + 1
# # print c + reversWord(a[j:])

# # print " ".join(map(lambda x:x[::-1],a.split(" ")))

# # a = 'APPPLLP'
# # print a.count('A') < 2 and 'LLL' not in a


        
# # s = 'abcdefg'
# # k = 2
# # l = len(s)
# # c = ''
# # d = l / k
# # for i in range(d):
# # 	if i % 2 == 0: 
# # 		c = c + s[i*k:(i+1)*k][::-1]
# # 		print c
# # 	else: 
# # 		c = c + s[i*k:(i+1)*k]
# # 		print c
# # if d % 2 == 0: c = c + s[d*k:][::-1]
# # else: c = c + s[d*k:]
# # print c
            
# # s = '{()[]{}}'                     
# # sta = [s[0]]
# # print sta
# # d = {'(':')','[':']','{':'}'}
# # for i in range(1,len(s)):
# # 	a = sta.pop()
# # 	print a
# # 	if d[str(a)]!=s[i]:
# # 		sta.append(a)
# # 		sta.append(s[i])

# # a = "ebcbbececabbacecbbcbe"
# # for x in range(len(a)/2):
# # 	print a[x], a[-(x+1)]

# # class Solution(object):
# #     def validPalindrome(self, s):
# #         """
# #         :type s: str
# #         :rtype: bool
# #         """
# #         l = len(s)
# #         rev = s[::-1]
# #         if s == rev: return True
# #         for i in xrange(len(s)):
# #             if s[i] != rev[i]:
# #                 print s[i:-(i+1)],rev[i+1:-i],s[i+1:-i],rev[i:-(i+1)]
# #                 return s[i:l-i-1] == rev[i+1:l-i] or s[i+1:l-i] == rev[i:l-i-1]
# #         return True
# class Solution(object):
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         # s = '11'
#         if n == 1: return '1'
#         if n == 2: return '11'
#         out = '11'
#         out1 =''
#         for x in range(3,n+1):
#             j = 0
#             print 'nth = ', x
#             for i in range(len(out)-1):
#                 print '  ith = ', i,j
#                 if out[i] != out[i+1]: 
#                     out1 = out1 + str(i-j+1) + str(out[i])
#                     print 'j-i+1', j-i+1
#                     j = i + 1
#                     if i+1 == len(out)-1:
#                         out1 = out1 + '1' + str(out[i+1])
#                         print '    final out from not equal', out1
#                         print '\n'
#                     	break
#                     print 'out1 not equal', i,out1
#                     # j = i
#                 else: 
#                     if i+1 ==len(out)-1:
#                 	    out1 = out1 + '2' + str(out[i])
#                 	    print '    final out from equal', out1
#                 	    print '\n'
#                 	    break
#             out = out1
#             out1 = ''
#         return out
# a = Solution()
# s = 6
# print a.countAndSay(s)
# out = '12345'
# # print str(len(out[1:3]))


# s = '     '
# print s.split(" ")
# print len(s.split(" ")[-1])
# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         l =len(s)
#         v = 'aeiouAEIOU' 
#         if l==0: return ''
#         s1 = list(s)
#         i = 0
#         j = l-1
#         iReady = False
#         jReady = False
#         while i < j:
#             if (not iReady) and (s1[i] not in v):
#                 i += 1
#             else: iReady = True
            
#             if (not jReady) and (s1[j] not in v):
#                 j -= 1
#             else: jReady = True
            
#             if iReady and jReady:
#                 temp = s1[i]
#                 s1[i] = s1[j]
#                 s1[j] = temp
#                 iReady = False
#                 jReady = False
#                 i += 1
#                 j -= 1 
#         return ''.join(s1)
# a = 'qqq'
# s = Solution()
# print s.reverseVowels(a)



# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 0
#         for num in nums:
#             res = num ^ res
#             print res
#         return res

# a = [1,2,3,4,5,6,6,5,3,2,1]
# s = Solution()
# print s.singleNumber(a)

# print 5 ^ 12

from collections import OrderedDict
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # dp = OrderedDict()
        # for x in pattern:
        #     if dp.has_key(x):
        #         dp[x] = dp[x] + 1
        #     else: dp[x] = 1
        # ds = OrderedDict()
        # s = str.split()
        # for x in s:
        #     if x!='':
        #         if ds.has_key(x): ds[x] = ds[x] + 1
        #         else: ds[x] = 1
        # sv = ds.values()
        # sp = dp.values()
        # print ds,sv, dp,sp
        # # if sorted(sv) != sorted(sp): return False
        # if sv!= sp: return False
        # else: return True
        s = pattern
        print map(s.find,s)
        t = str.split()
        print map(t.index,t) 
        return map(s.find, s) == map(t.index, t)

a = 'abaaaaaa'
b = "dog cat cat     fd fg"
s = Solution()
print s.wordPattern(a,b)