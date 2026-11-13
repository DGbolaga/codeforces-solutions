test_case = int(input())

for _ in range(test_case):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # operation
    for i in range(n):
        a[i] = max(a[i], b[i])

    for j in range(n-1, -1, -1):
        if j-1 >= 0:
            a[j-1] = max(a[j-1], a[j])

    prefixsum = [a[0]]
    for t in range(1, n):
        prefixsum.append(prefixsum[t-1] + a[t])

    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 2
        r -= 1
        if l >= 0:
            ans.append(str(prefixsum[r] - prefixsum[l]))
        else:
            ans.append(str(prefixsum[r]))

    print(" ".join(ans))



   
