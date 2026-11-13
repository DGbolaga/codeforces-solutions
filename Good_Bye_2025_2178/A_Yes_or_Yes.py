n = int(input())
while n:
    st = input()
    t = [st[0]]
    len_st = len(st)
    cont = True
    for i in range(1, len_st):
        if st[i] == 'Y' and t[-1] == 'Y':
            print('NO')
            cont = False
            break 
        elif st[i] == 'N' and t[-1] == 'N':
            continue
        else:
            t.append('Y')
    
    if cont:
        print('YES')
    
    
    n-=1