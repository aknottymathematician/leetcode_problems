class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mSum = 0
        mStart = 0
        mCount = float('inf')
        
        for mEnd in range(len(nums)):
            mSum += nums[mEnd]
            
            while mSum >= target:
                mCount = min(mCount, mEnd-mStart+1)
                mSum -= nums[mStart]
                mStart += 1
        if mCount == float('inf'):
            return 0
        return mCount
    
