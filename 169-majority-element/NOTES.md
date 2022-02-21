## Boyer Moore Majority vote algorithm

Initialize an element m and a counter i with i = 0
For each element x of the input sequence:
If i = 0, then assign m = x and i = 1
else if m = x, then assign i = i + 1
else assign i = i − 1
Return m
