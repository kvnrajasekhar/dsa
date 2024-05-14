#link: https://leetcode.com/problems/path-with-maximum-gold

class Solution:
    def getMaximumGold(self, grid):
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 0):
                return 0
            
            gold = grid[r][c]
            grid[r][c] = 0  # Mark as visited
            
            max_gold = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_gold = max(max_gold, gold + dfs(r + dr, c + dc))
            
            grid[r][c] = gold  # Revert back to original value
            return max_gold
        
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        
        return max_gold
