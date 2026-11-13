n = int(input())

for _ in range(n):
    len_n = int(input())
    arr = list(map(int, input().split()))

    if arr[0] ==  -1: arr[0] = arr[len_n-1]
    if arr[len_n-1] == -1: arr[len_n-1] = arr[0]

    for i in range(len_n):
        if arr[i] == -1:
            arr[i] = 0
    
    print(abs(arr[len_n-1] - arr[0]))
    print(" ".join(map(str, arr)))