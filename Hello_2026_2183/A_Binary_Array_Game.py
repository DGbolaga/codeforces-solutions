c = int(input())
for _ in range(c):
    n = int(input())
    arr = list(map(int, input().split()))

    # remove all 10.
    print("Alice" if (arr[0] == 1 or arr[-1] == 1) else 'Bob')