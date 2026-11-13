from collections import deque 

t = int(input())
for _ in range(t):
    x = 3 * int(input())
    arr = deque([i for i in range(1, x+1)])
    result = []
    # take the first value and last 2 value.
    while arr:
        result.append(arr.popleft())
        a, b = arr.pop(), arr.pop()
        result.append(b)
        result.append(a)
    
    print(" ".join(map(str,result)))
