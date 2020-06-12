n = int(input())
a = list(map(int, input().split()))

Alice = 0
Bob = 0

for i in range(n):
    if i % 2 == 0:
        Alice += max(a)
        a.remove(max(a))
    else:
        Bob += max(a)
        a.remove(max(a))

print('{0}'.format(Alice - Bob))
