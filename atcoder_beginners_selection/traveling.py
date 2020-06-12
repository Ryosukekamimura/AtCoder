n = int(input())
prev_t = 0
for i in range(n):
    t, x, y=map(int, input().split())
    if (x + y) > (t - prev_t) or (x + y + (t )) % 2 != 0:
        print("No")
        exit()
    prev_t = t
print("Yes")