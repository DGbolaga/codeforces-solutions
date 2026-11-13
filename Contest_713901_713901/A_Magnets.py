
cnt =0
prev = []
for _ in range(int(input())):
    if not prev:
        cnt += 1
        prev.append(input())
    else:
        x = input()
        if prev[-1] == x:
            prev.append(x)
        else:
            prev = [x]
            cnt += 1

print(cnt)
