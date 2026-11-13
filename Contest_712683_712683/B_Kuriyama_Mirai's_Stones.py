n = int(input())
v = list(map(int, input().split()))
prefix_v = [0]
for i in v:
    prefix_v.append(prefix_v[-1]+i)

u = sorted(v)
prefix_u = [0]
for j in u:
    prefix_u.append(prefix_u[-1]+j)

m = int(input())
for _ in range(m):
    typ, l, r = list(map(int, input().split()))

    if typ == 1:
        # do first
        print(prefix_v[r]-prefix_v[l-1])
    else:
        # do second
        print(prefix_u[r]-prefix_u[l-1])
