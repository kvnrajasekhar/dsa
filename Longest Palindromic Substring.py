# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def longest(a, b):
        #     if len(a) > len(b):
        #         return a
        #     return b
        res=""
        prev=""
        size=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                res+=s[j]
                if res == res[::-1] and len(res)>size:
                    prev=res
                    size=len(res)
            res=""
        return prev
