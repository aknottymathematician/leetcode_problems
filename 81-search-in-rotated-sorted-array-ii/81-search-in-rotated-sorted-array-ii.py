class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def helper(left, right):

            if left > right:
                return False
            
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            else:

                if nums[mid] < nums[right]:
                    # right half is sorted
                    
                    if nums[mid] < target <= nums[right]:
                        return helper(left=mid+1, right=right)
                    else:
                        return helper(left=left, right=mid-1)
                        
                elif nums[mid] > nums[right]:
                    # left half is sorted
                    
                    if nums[left] <= target < nums[mid]:
                        return helper(left=left, right=mid-1)
                    else:
                        return helper(left=mid+1, right=right)
                    
                else:
                    # repeated at mid and right, discard the rightmost element
                    return helper(left=left, right=right-1)
        # ------------------------------------------------------
                    
        return helper(left=0, right=len(nums)-1)