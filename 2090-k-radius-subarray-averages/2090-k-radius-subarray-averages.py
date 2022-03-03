class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1]*len(nums)
        wStart = 0
        wSum = 0
        radius = 2*k+1
        for wEnd in range(len(nums)):
            wSum += nums[wEnd]
            if (wEnd-wStart+1) >= radius:
                result[wStart+k] = wSum//radius
                wSum -= nums[wStart]
                wStart+=1
        return result
