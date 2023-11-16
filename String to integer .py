# problem : https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        n=len(s)
        k=0
        temp='+'
        while k<n and s[k]==" ":
            k+=1
        if k<n and (s[k]== '+' or s[k]=='-'):
            temp=s[k]
            k+=1
        while k < n:
            if s[k].isdigit():
                res = res*10 + int(s[k])
                k+=1    
            else:
                break
        res = res if temp=="+" else -res
        num = max(min((res), 2**31 - 1), -2**31)    
        return num
