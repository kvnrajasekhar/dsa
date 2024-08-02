#link:https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        maxl=height[l]
        maxr=height[r]
        res=0
        #using two pointer 
        while l<r:
            if maxl<maxr: # increment l until l<=r
                l+=1
                maxl=max(maxl,height[l])
                res+= maxl-height[l]
            else: # decrement r if l>r
                r-=1
                maxr=max(maxr,height[r])
                res+=maxr-height[r]
        return res
