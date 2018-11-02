def findCelebrity(n):
	if n < 2: return -1
	x = 0 # x is the possible celebrity
	for i in xrange(1,n):
		if knows(x, i):
			x = i
	for i in xrange(n):
		if x != i and (knows(x, i) or not knows(i, x)): return -1
	return x

def knows(x,i):
	if (x,i) in [(0,1),(1,2),(4,5),(0,3),(1,3),(2,3),(4,3),(5,3)]: return True
	return False
print findCelebrity(5)