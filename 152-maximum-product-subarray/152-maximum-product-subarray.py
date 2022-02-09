class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        maxVal = max(nums)
        for num in nums:
            if num==0:
                curMax, curMin = 1,1
                continue
                
            curProd = curMax * num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(curProd, curMin*num, num)
            maxVal = max(curMax, maxVal)
        return maxVal