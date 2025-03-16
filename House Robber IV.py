#link : https://leetcode.com/problems/house-robber-iv/description/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        if len(nums) == 2 and k==1:
            return min(nums)
        '''l , r, = 0, len(nums)
        done = k 
        capability = []
        for i in range(len(nums)):
            end = i +2 
            temp = done
            while end < len(nums) and temp > 0:
                capability.append(max(nums[i],nums[end]))
                end += 2
                done -= 1
        return min(capability) if capability else 0'''
        l, r = min(nums), max(nums)
        def can(mid):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        while l < r:
            mid = (l + r) // 2
            if can(mid):
                r = mid
            else:
                l = mid + 1
        return l

        
        
