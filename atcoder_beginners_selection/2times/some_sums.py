n, a, b = map(int, input().split())

def digitSum(num):
    s = str(num)
    array  = list(map(int, s))
    return int(sum(array))

total = 0

for i in range(n+1):
    k = digitSum(i)
    if a <= k and k <= b:
        total += i
    else:
        continue

print(total)