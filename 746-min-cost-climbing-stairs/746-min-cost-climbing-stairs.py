class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)-1
        dp = (n+1)*[0]
        dp[0] = cost[0]
        
        dp[1] = cost[1]
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])