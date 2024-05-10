#link :https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction={}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                fraction[arr[i]/arr[j]] = [(arr[i]),(arr[j])]
        fractions_list=sorted(fraction)
        value = fraction[fractions_list[k-1]]
        return value
