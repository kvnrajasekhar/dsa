# link : https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -1
        l=0
        r=len(height)-1
        maxi_area=0
        while l<r:
            d=r-l
            area = d*(min(height[r],height[l]))
            maxi_area=max(maxi_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi_area
        
