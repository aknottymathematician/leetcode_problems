class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # result = []
        # wStart = 0
        # wSum = 0
        # radius = 2*k+1
        # for wEnd in range(len(nums)):
        #     wSum += nums[wEnd]
        #     if (wEnd-wStart+1) >= radius:
        #         result[wStart+k] = wSum//radius
        #         wSum -= nums[wStart]
        #         wStart+=1
        # return result

        res = [-1]*len(nums)

        left, curWindowSum, radius = 0, 0, 2*k+1
        for right in range(len(nums)):
            curWindowSum += nums[right]
            if (right-left+1 >= radius):
                res[left+k] = curWindowSum//radius
                curWindowSum -= nums[left]
                left += 1
        return res