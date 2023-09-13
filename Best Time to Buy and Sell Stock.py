# link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_diff =0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         current_diff = prices[j] - prices[i]
        #         max_diff=max(current_diff,max_diff) 
        # return max_diff
        prof=0
        buy=prices[0]
        for i in prices[1:]:
            buy=min(buy,i)
            prof=max(prof,i-buy)
        return prof
        
