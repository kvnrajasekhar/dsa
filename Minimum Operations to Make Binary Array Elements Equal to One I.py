#lnk :https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:    
        op = 0
        for i in range(len(nums)-2): # 011100
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                op += 1
        return op if (nums[-2]== 1 and nums[-1]==1) else -1
