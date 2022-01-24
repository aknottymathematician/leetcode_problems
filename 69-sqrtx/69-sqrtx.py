class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l = 0
        u = x
        while l<=u:
            mid = l+(u-l)//2
            if mid*mid == x and (mid+1)*(mid+1)>x:
                return mid
            if mid*mid > x:
                u = mid-1
                
            else:
                l = mid+1
        return l-1