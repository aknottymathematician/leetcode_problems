class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = float('inf'), 0
        
        for price in prices:
            buy = min(buy, price)
            ans = max(ans, price -buy)
            
        return ans