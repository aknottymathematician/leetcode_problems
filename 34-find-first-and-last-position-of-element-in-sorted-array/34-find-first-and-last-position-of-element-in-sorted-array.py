class Solution:
    def firstSearch(self, nums, x):
        l = 0
        r = len(nums)-1
        first = -1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==x:
                first = mid
                r = mid-1
            elif nums[mid]>x:
                r=mid-1
            elif nums[mid]<x:
                l = mid+1
        return first
    
    def lastSearch(self, nums, x):
        l = 0
        r = len(nums)-1
        last = -1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==x:
                last = mid
                l = mid+1
            elif nums[mid]>x:
                r = mid-1
            elif nums[mid]<x:
                l = mid+1
        return last
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstSearch(nums, target)
        last = self.lastSearch(nums, target)
        
        return [first, last]