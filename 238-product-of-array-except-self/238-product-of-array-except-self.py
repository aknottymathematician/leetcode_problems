class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        
        left = 1
        for num in nums:
            product.append(left)
            left = left*num
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            product[i]=product[i]*right
            right = right*nums[i]
            
        return product