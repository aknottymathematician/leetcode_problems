class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        mSum = 0
        mCount = 0
        mStart = 0

        for mEnd in range(len(arr)):
            mSum += arr[mEnd]
            if mEnd >= k:
                mSum -= arr[mStart]
                mStart +=1
            if (mSum//k) >= threshold and (mEnd-mStart+1)==k:
                mCount += 1

        return mCount