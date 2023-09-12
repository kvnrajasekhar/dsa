# link : https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        k=str(x)
        p=[]
        if x<0:
            l=k[0]
            p=l+(k[(len(k)-1):0:-1])
        else:
            l=k[0]
            p=[]
            p=(k[(len(k)-1):0:-1])+l
        rev=int(p)
        if rev >= 2147483647 or rev <= -2147483648:
            return 0
        else:
            p=int(p)
            return p
