n = int(input())

for _ in range(n):
    n, s, x = list(map(int, input().split()))

    arr = list(map(int, input().split()))
    total = sum(arr)

    if total > s:
        print("NO")
    else:
        print("YES" if (s - total) % x == 0 else "NO")