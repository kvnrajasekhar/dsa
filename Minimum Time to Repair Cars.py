#link : https://leetcode.com/problems/minimum-time-to-repair-cars/description/
class Solution:
    def can(self,ranks,m,cars):
        cnt = 0
        for r in ranks:
            cnt += int(math.sqrt((m//r)))
        return cnt >= cars
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mintime = 0
        n = len(ranks)
        l = 1
        h = min(ranks) * cars * cars
        while l <= h:
            m = l +(h-l)//2
            if self.can(ranks,m,cars):
                mintime = m
                h = m - 1
            else:
                l = m+1
        return int(mintime)

        
        
