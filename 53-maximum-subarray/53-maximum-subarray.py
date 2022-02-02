class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currNum = 0
        
        for n in nums:
            if currNum < 0:
                currNum = 0
            
            currNum += n
            maxSub = max(maxSub, currNum)
        
        return maxSub