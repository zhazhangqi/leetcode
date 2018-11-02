import heapq
def maxMin(operations, x):
	dic = collections.defaultdict(int)
	res = []
	for i, op in enumerate(operations):
		if op == 'push':
			if x[i] in dic:
				res.append(res[-1])
				dic[x[i]] += 1
			else:
				dic[x[i]] += 1
				res.append(max(dic.keys())*min(dic.keys()))	
			
		if op == 'pop':
			dic[x[i]] -= 1
			if dic[x[i]] == 0:
				del dic[(x[i])]
				res.append(max(dic.keys())*min(dic.keys()))
			else:
				res.append(res[-1])



op = ['push','push','push','pop']
X = [1,3,3,3]
print maxMin(op, X)