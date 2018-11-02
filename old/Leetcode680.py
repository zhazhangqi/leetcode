class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mark = 0
        mw = 0
        ii = 0
        jj = 0
        i = 0
        j = 1
        while i < len(s)/2:
            if s[i]!=s[-j]:
                if mark > 0:
                    if mw == 1: 
                        mw = 0
                        i = ii + 2
                        j = jj + 1
                    # print 'mark i,j',i,j
                    else: return False
                else:
                    mark = mark + 1
                    if s[i+1] == s[-j] and s[i] == s[-(j+1)]: 
                        ii = i
                        jj = j                        
                        i = i + 1
                        j = j + 2
                        mw = 1
                    elif s[i+1] == s[-j]: 
                        i = i + 2
                        j = j + 1
                    elif s[i] == s[-(j+1)]: 
                        i = i + 1
                        j = j + 2
                    else: 
                        # print 'cannot i,j',i,j
                        return False
            else:
                j += 1
                i += 1
        return True