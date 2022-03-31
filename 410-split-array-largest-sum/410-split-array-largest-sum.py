class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(Q):
            if max(nums) > Q: return False
            acc, ans = 0, 1
            for num in nums:
                if acc + num <= Q:
                    acc += num
                else:
                    acc = num
                    ans += 1
            return ans <= m
        
        beg, end = max(nums) - 1, sum(nums)
        while beg + 1 < end:
            mid = (beg + end)//2
            if check(mid):
                end = mid
            else:
                beg = mid
        
        return end