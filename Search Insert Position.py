#https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0 # iam going with binary search method 
        e=len(nums)-1
        while s<=e:
            mid = (s+e) // 2
            if nums[mid] > target:
                e=e-1
            elif nums[mid]<target:
                s=s+1
            else:
                return mid
        return s # if target is not in the array 
