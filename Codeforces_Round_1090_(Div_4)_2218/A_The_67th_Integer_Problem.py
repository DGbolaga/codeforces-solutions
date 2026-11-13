t = int(input())
for _ in range(t):
    x = int(input())
    print(max(x, x+1) if x < 67 else x)