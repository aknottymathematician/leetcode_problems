class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mStart = 0
        mLen = 0
        charIdxMap = {}
        
        for mEnd in range(len(s)):
            rChar = s[mEnd]
            
            if rChar in charIdxMap:
                mStart = max(mStart, charIdxMap[rChar]+1)
            
            charIdxMap[rChar] = mEnd
            mLen = max(mLen, mEnd-mStart+1)
        
        return mLen