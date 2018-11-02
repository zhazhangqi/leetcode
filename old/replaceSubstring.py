# replace the substring with another string, return all the possiable answer
def replace(s, t, r):
	dic = {}
	res = []
	for i, x in enumerate(t): dic[x] = r[i]
	def dfs(index, line):
		if index == len(s): 
			res.append(line)
			return
		canreplace = False
		for sub in dic:
			ls = len(sub)
			if index + ls <= len(s) and s[index:index+ls] in dic:
				canreplace = True
				dfs(index+ls, line + dic[s[index:index+ls]])
		if not canreplace:
			dfs(index + 1, line + s[index])
	dfs(0, '')
	return res
print replace('abbbb', ['b', 'bb'], ['c', 'dd'])



	# replace(s, '')
