# link : https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = ""
        self.paran_generator(n, n, current, res) 
        return res
    def paran_generator(self, left, right, current, res):
        if left == 0 and right == 0:
            res.append(current)
            return res
        if left > 0:
            self.paran_generator(left - 1, right, current + "(", res)
        if right > left:
            self.paran_generator(left, right - 1, current + ")", res)
        return res
