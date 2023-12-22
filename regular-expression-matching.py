# link :  https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # flag=0
        # if len(s)!=len(p):
        #     return False
        # for i in p:
        #     if i in s:
        #         flag=1
        #     if flag and ("." in p) or ("*" in p) or (("." in p) and ("*" in  p)):
        #         return True
        # return False
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = (dp(i, j + 2) or (first_match and dp(i + 1, j)))
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
