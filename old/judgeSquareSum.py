def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    def sqrt(t):
        l = 0
        r = t
        while l <= r:
            m = (l + r)/2
            if m*m == t: 
                print m 
                return True
            if m*m < t:
                l = m + 1
            else: r = m - 1
        return False
            
    i = 0
    while i*i <= c:
        if sqrt(t = c - i * i): 
            print i    
            return True
        i += 1
    return False
print judgeSquareSum(2147483642)