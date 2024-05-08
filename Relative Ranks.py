#link : https://leetcode.com/problems/relative-ranks/description/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_list = sorted(score,reverse=True)
        ranks = {}
        for i in range(len(sort_list)):
            if i==0:
                ranks[sort_list[i]]= "Gold Medal"
            elif i==1:
                ranks[sort_list[i]]= "Silver Medal"
            elif i==2:
                ranks[sort_list[i]]= "Bronze Medal"
            else:
                ranks[sort_list[i]] = str(i+1)
        final = []
        for i in score:
            final.append(ranks[i])
        return final
