class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: return []
        res = []
        def helper(res, path, num, target, pos, pre, val):
            if pos == len(num) and val == target:
                res.append(path)
                return
            for i in xrange(pos, len(num)):
                # if i != pos and num[pos] == '0': break
                cur = int(num[pos:i+1])
                if pos == 0:
                    helper(res, path + str(cur), num, target, i + 1, cur, cur)
                else:
                    helper(res, path + "+" + str(cur), num, target, i + 1, cur, val + cur)
                    helper(res, path + "-" + str(cur), num, target, i + 1, -cur, val - cur)
                    helper(res, path + "*" + str(cur), num, target, i + 1, pre * cur, val - pre + pre * cur)
        helper(res, '', num, target, 0, 0, 0)
        return res

a = Solution()
print a.addOperators('105',5)
