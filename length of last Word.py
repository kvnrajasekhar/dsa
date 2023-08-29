#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wcnt=0
        n=len(s)
        i=n-1
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            wcnt+=1
            i=i-1
        return wcnt
