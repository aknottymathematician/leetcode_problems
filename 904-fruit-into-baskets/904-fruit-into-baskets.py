class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mStart = 0
        mLen = 0
        charFreq = collections.Counter()
        
        for mEnd in range(len(fruits)):
            rChar = fruits[mEnd]
            if rChar not in charFreq:
                charFreq[rChar]=0
            charFreq[rChar] +=1
            
            while len(charFreq)>2:
                lChar = fruits[mStart]
                charFreq[lChar]-=1
                if charFreq[lChar] == 0:
                    del charFreq[lChar]
                mStart+=1
            mLen = max(mLen, mEnd-mStart+1)
        
        return mLen