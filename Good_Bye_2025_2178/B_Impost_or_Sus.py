n = int(input())
for _ in range(n):
    w = list(input())
    len_w = len(w)
    ans = 0
    for i, ch in enumerate(w):
        if i == 0 or i == len_w-1:
            if ch == 'u':
                w[i] = 's'
                ans += 1
        else:
            if i+1 < len_w and ch == 'u' and w[i+1] == 'u':
                w[i+1] = 's'
                ans +=1
    print(ans)

