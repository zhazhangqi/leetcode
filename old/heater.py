class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        print heaters
        heaters.sort()
        print heaters
        maxR = 0
        lens = len(heaters)-1
        for x in houses:
            minR = min(abs(x-heaters[lens]),abs(x-heaters[0]))
            l = 0
            h = lens
            if h == l: m = 0 
            while h >= l:    
                m = (h+l)/2
                if x == heaters[m]: 
                    minR = 0
                    break
                if x > heaters[m]: l = m + 1
                if x < heaters[m]: h = m - 1            
            if l==0 : minR = min(minR, abs(x-heaters[l]))
            elif l > lens: minR = min(minR, abs(x-heaters[l-1]))
            else: minR = min(minR,abs(x-heaters[l]),abs(x-heaters[l-1]))
            maxR = max(maxR, minR)
            print 'x= ',x, '; m = ',m, '; minR = ',minR
        return maxR
# houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
houses = [343098142,456880399,534827968,280090412,195400260,589673557,6441594,889688008,57716395]
heaters  = [14119113,515204530,388471006,681910962,904797942,400285365,322842082,463179852,828530767]
# houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
s = Solution()
print s.findRadius(houses,heaters) 

# y=[1,3,5,7,9]
# x =5
# l = 0
# h = len(y)-1
# while h >= l:    
#     m = (h+l)/2
#     # print m,y[m]
#     # print  "l = ",l, "; h = ",h,'; m = ',m   
#     if x == y[m]: break
#     if x > y[m]: l = m + 1
#     if x < y[m]: h = m - 1 

# print  "l = ",l, "; h = ",h,'; m = ',m   
