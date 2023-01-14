class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k in range(0,len(nums),1):
            for l in range(k+1,len(nums),1):
                if(nums[k]+nums[l]==target):
                    return [k,l]
                else:
                    continue
