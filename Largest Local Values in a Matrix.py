#link:https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0] *(n-2) for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                ans[i][j]=grid[i][j]
                for k in range(3):
                    for l in range(3):
                        ans[i][j]= max(ans[i][j],grid[i+k][j+l])
        return ans

