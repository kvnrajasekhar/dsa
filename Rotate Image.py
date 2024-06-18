#link: https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):#making transpose
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:#after transpose reversing the rows
            left, right = 0, len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
