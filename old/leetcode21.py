#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printl(self):
        while self:
            print self.val
            self = self.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        temp1 = l1
        temp2 = l2
        while (temp1 != None) and (temp2 != None):
            if temp2.val >= temp1.val:
                temp = temp1.next
                temp1.next = temp2
                temp1 = temp2
                temp2 = temp
        return l1

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)
l1.printl()
s = Solution()
l3 = s.mergeTwoLists(l1,l2)
l3.printl()


