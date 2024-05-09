#link:https://leetcode.com/problems/maximize-happiness-of-selected-children/
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # time limit exceeded fot his code so commented but it works
        child_happiness = 0
        happiness.sort(reverse=True)
        # for i in range(k):
        #     child_happiness += happiness[0]
        #     del(happiness[0])
        #     happiness = [*map(lambda x : x-1 if x!=0 else 0 ,happiness)]
        # return child_happiness

        #here we decrease each element by its index number 
        i=0
        while k>0:
            happiness[i] = max(happiness[i]-i,0)
            child_happiness += happiness[i]
            i+=1
            k-=1
        return child_happiness
