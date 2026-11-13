t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    if y//2 + x != y:
        print("YES")
    else:
        print("NO")