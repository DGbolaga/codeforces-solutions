n = int(input())

def rev(start, stop, arr):
    i, j = start, stop 

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    
    return arr
    
        

for _ in range(n):
    x = int(input())
    arr = list(map(int, input().split()))

    mp = {arr[i]: i for i in range(x)}
    
    start = 0
    used = False
    while x > 0:
        if mp[x] != start:
            print(" ".join(map(str, rev(start, mp[x], arr))))
            used = True
            break
        x -= 1
        start += 1
    
    if not used:
        print(" ".join(map(str, arr)))

    
            
   


    


