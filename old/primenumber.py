def generate_primeNumber(n):
	res = []
	prime = [True for _ in xrange(0, n+1)]
	i = 2
	while i * i <= n:
		if prime[i]:
			for j in xrange(2*i, n+1, i):
				prime[j] = False
		i += 1
	for x in xrange(2,n + 1):
		if prime[x]: res.append(x)
	return res

def check_primeNumber(n):
	if n < 2: return False
	if n <= 3: return True
	if n % 2 == 0 or n % 3 == 0: return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % (i + 2) == 0: return False
		i += 6
	return True
print check_primeNumber(9)
print generate_primeNumber(50)


        
 