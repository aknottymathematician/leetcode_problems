class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        total = 0
        
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
            else:
                dp[i]=0
        
            total += dp[i]
    
        return total