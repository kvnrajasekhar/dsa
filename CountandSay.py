#link ; https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        def next(s):
            res = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                res.append(str(count))
                res.append(s[i])
                i += 1  
            return ''.join(res)

        curr = "1"
        for _ in range(1, n):
            curr = next(curr)
        return curr
