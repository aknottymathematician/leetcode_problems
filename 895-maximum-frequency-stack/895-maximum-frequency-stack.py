class FreqStack:

    def __init__(self):
        self.freq= Counter()
        self.stacks = defaultdict(list)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        freqVal = self.freq[val]+1
        self.freq[val] = freqVal
        self.maxFreq = max(self.maxFreq, freqVal)
        self.stacks[freqVal].append(val)

        
    '''
    pop(self): first of all, element we are looking for is last element in self.stacks[self.maxfreq], so we pop it. 
    Also we need to decrease frequency of this element. 
    Finally, if number of elements with highest frequency equal to 0, we can remove this stack. Then we return x.
    '''
    def pop(self) -> int:
        val = self.stacks[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.stacks[self.maxFreq]:
            self.maxFreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()