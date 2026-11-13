c = int(input())
for _ in range(c):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    if all(arr[i] <= arr[i+1] for i in range(n-1)):
        print("YES")
        continue 
    elif k == 1:
        print("NO")
    else:
        print("YES")
