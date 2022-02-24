class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        val = 0
        for i in nums:
            if not i in res:
                res[i] = 1
            else:
                res[i]+=1
        for k in res:
            if res[k]==1:
                return k
        return -1