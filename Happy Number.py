# https://leetcode.com/problems/happy-number/description/
class Solution:
    def isHappy(self, n: int) -> bool:
        add=0
        hashmap=set()
        sums=[n] # optional step 
        while n != 1:
            if n in hash:
                return False
            hashmap.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
