n, y= map(int, input().split())


for i in range(n+1):
    for j in range(n+1):
            if 10000*i+5000*j+1000*(n-i-j) == y and n-i-j>=0:
                print('{0} {1} {2}'.format(i, j, n-i-j))
                exit()
            else:
                continue
            break
    else:

        continue
    break
print('-1 -1 -1')
