import math

t = int(input())

for _ in range(t):
    # n = number of paintings
    # c = amount of used square centimeters of cardboard
    # s = size of paintings
    n, c = list(map(int, input().split()))
    s = list(map(int, input().split()))

    # 50 = (3 + w)**2 + (2 + w)**2 + (1 + w)**2
    # 50 = 9 + 6w + w**2 + 4 + 4w + w**2 + 1 + 2w + w**2
    # 50 = (9 + 4 + 1) + (6w + 4w + 2w) + 3(w**2)
    # 50 = 3w**2 + 12w + 14
    # 0  = 3w**2 + 12w + 14 - c
    # w**2 + 4w - 12 
    # (w-2)(w+6) = 0
    # 2, -6
    # the final answer will be +2 divided by 2 = 1.

    # 100 = (6 + w)**2
    # 500 = (2 + w)**2 + (2 + w)**2 + (2 + w)**2 + (2 + w)**2 + (2 + w)**2


    #   a        b            c
    #3(w**2) - 2(sum)w  + c - sum([x**2 for x in s]) = 0
    a = n
    b = 0
    sq = 0

    for i in s:
        b += 2*i 
        sq += i**2
    
    C = sq - c
    # print(a, b, C)
    # print(math.sqrt(b**2 - 4*a*C))
    res1 = (-b + math.sqrt(b**2 - 4*a*C)) / (2*a)
    res2 = (-b - math.sqrt(b**2 - 4*a*C)) / (2*a)

    # print(res1, res2)
    ans = res1 // 2 if res1 > 0 else res2 // 2

    print(int(ans))





    

    



    





    
