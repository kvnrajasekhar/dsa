#link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
class Solution:
    def maxScore(self, s: str) -> int:
        maxi=0
        for i in range(len(s)):
            left = s[0:i+1]
            right = s[i+1:len(s)]
            if right:
                maxi=max(maxi, left.count("0") + right.count("1"))
        return maxi
