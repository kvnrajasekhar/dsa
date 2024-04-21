# link : https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        closest_sum = float('inf')
        n = len(nums)
        
        for i in range(n - 2):  # Loop through the array, leave at least two elements for the other pointers
            left = i + 1
            right = n - 1
            
            while left < right:  # Two-pointer technique
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return closest_sum  # If we find exact match, no need to continue, return immediately
        
        return closest_sum
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         slist = []
#         n=len(nums)
#         for i in range(n):
#             if i < n-3 :
#                 sum_ = nums[i]+nums[i+1]+nums[i+2]
#                 slist.append(sum_)
#             if i == n-3:
#                 sum_ = nums[n-1]+nums[n-2]+nums[n-3]
#                 slist.append(sum_)
#         def close(num,arr):
#             curr = arr[0]
#             for index in range (len (arr)):
#                 if abs (num - arr[index]) < abs (num - curr):
#                     curr = arr[index]
#             return curr
#         close = close(target,slist)
#         return close
