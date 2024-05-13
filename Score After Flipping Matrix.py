# link : https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # res = ROWS * 2** (COLS - 1)
        # for c in range(1, COLS):
        #     cnt = 0
        #     for r in range (ROWS):
        #         if grid[r][c] != grid[r][0]:
        #             cnt += 1
        #     cnt = max(cnt, ROWS - cnt)
        #     res += cnt * (2** (COLS - c - 1))
        # return res

        # Flip rows 
        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = 0 if grid[r][c] else 1
        # Flip cols if no.of 0's are more than no.of 1's
        for c in range(COLS):
            one_cnt = 0
            for r in range(ROWS):
                one_cnt += grid[r][c]
            if one_cnt < ROWS - one_cnt:
                for r in range (ROWS):
                    grid[r][c] = 0 if grid[r][c] else 1
        res = 0
        for r in range (ROWS):
            for c in range(COLS):
                res += grid[r][c] << (COLS - c - 1)
        return res
