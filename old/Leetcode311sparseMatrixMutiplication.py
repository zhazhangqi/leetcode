def multiply(A, B):
	m = len(A)
	n = len(A[0])
	nb = len(B[0])
	if n != len(B): return []
	# res1 = [[0]*nb]*m  # doing this make every line is the same object, kind of like a = b = [], makes a and b are the same object
	res2 = [[0]*nb for _ in xrange(m)]

	for i in xrange(m):
		for j in xrange(n):
			if A[i][j]:
				for k in xrange(nb):
					res1[i][k] += A[i][j] * B[j][k]
					res2[i][k] += A[i][j] * B[j][k]
					print 'res1',i, j, k, res1,
					print 'res2',i, j, k, res2
	return res2

A = [[1,0,0],[-1,0,3]]
B = [[7,0,0],[0,0,0],[0,0,1]]
print multiply(A,B)