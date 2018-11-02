# # import bisect
# # a = [0,1,2,2,3,4,5,6,7]
# # print bisect.bisect_left(a, 2)
# # print bisect.bisect_right(a, 2)
# # print a
# def fullJustify(words, maxWidth):
#     n = len(words) 
#     res = []
#     idx = 0
#     while idx < n:
#         count = len(words[idx])
#         last = idx + 1
#         while last < n and count + 1 + len(words[last]) <= maxWidth:
#             count += 1 + len(words[last])
#             last += 1
#         line = words[idx]
#         if last == n or last == idx + 1:
#             for i in xrange(idx+1, last):
#             	line = line + ' ' + words[i]
#             line = line + ' '*(maxWidth - count)
#         else:
#             diff = (last - idx - 1)
#             space = (maxWidth - count) / diff
#             extra = (maxWidth - count) % diff
#             for i in xrange(idx+1, last):
#                 if extra > 0:
#                     line = line + ' '*(space + 1 + 1) + words[i]
#                     extra -= 1
#                 else:
#                     line = line + ' '*(space + 1) + words[i]
#         res.append(line)
#         idx = last
#     return res

# print fullJustify(["a","b","c","d","e"], 3)
for x in xrange(5):
	print x
	x = 4
def hammingDistance(x, y):
	xor = x^y # get yi huo
	res = 0 
	while xor != 0:
		res += xor & 1 # mask with 1, if lower bit is 1, then return 1
		xor = xor >> 1 # xor move 1 bit to the right
	return res
print hammingDistance(13,7) 
