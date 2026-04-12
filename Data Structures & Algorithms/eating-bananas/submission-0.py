import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            t = 0
            for i in piles:
                t += math.ceil(float(i)/mid)

            if t<=h:
                r = mid -1
                res = mid
            if t>h:
                l = mid +1

            
        # print(res)
        return res

                


