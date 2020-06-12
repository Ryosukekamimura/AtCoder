n, y = map(int, input().split())


for i in range(n+1):
    for k in range(n+1):
        if 10000*i + 5000*k + 1000*(n-i-k) == y and n-i-k >= 0:
            print('{0} {1} {2}'.format(i, k, n-i-k))
            exit()
        else:
            continue

print('-1 -1 -1')