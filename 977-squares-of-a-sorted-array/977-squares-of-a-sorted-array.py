class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start = 0
        end = n-1
        squares = [0]*(n)
        highestIdx = n-1
        
        while start <= end:
            left = nums[start]*nums[start]
            right = nums[end]*nums[end]
            
            if left<right:
                squares[highestIdx] = right
                end-=1
            else:
                squares[highestIdx] = left
                start += 1
            highestIdx -= 1
        
        return squares