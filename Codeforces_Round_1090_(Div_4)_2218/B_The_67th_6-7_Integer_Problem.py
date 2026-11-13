t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    res = 0 
    for i in range(len(a)):
        if i != len(a)-1:
            res += -a[i]
        else:
            res += a[i]

    print(res)

