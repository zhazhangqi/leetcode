import time
time.time()
class Solution(object):
    def combine(self, n, k):
        # get all combination and then remove not good ones
        res = [[]]
        res1 = []
        for i in xrange(1,n+1):
            for j in xrange(len(res)):
                if len(res[j]) < k:
                    res += [res[j] + [i]]
        for x in res:
            if len(x) == k:
                res1.append(x)
        return res1
        # possible generate extral list
    def combine1(self, n, k):
        def helper(res, line, cad, k):
            if len(line) == k: 
                res.append([x for x in line])
                return
            for i, x in enumerate(cad):
                line.append(x)
                helper(res, line, cad[i+1:],k)
                line.pop()        
        cad = [i for i in range(1,n+1)]
        if k > n: return []
        if k == n: return [cad]
        
        res = []
        line = []
        helper(res, line, cad, k)
        return res

    def combine2(self, n, k):

        def helper(res, line, start, n, k):
            if k == 0: 
                res.append([x for x in line])
                return
            
            for i in xrange(start,n):
                line.append(i)
                helper(res, line, i + 1, n, k-1)
                line.pop()        

        res = []
        line = []
        helper(res, line, 1, n, k)
        return res    
a = Solution()
timestamp1 = time.time()
a.combine(19,17)
timestamp2 = time.time()
print "combine, This took %.3f seconds" % (timestamp2 - timestamp1)
timestamp1 = time.time()
a.combine1(19,17)
timestamp2 = time.time()
print "combine1, This took %.3f seconds" % (timestamp2 - timestamp1)
timestamp1 = time.time()
a.combine2(19,17)
timestamp2 = time.time()
print "combine2, This took %.3f seconds" % (timestamp2 - timestamp1)
