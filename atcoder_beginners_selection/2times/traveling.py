n = int(input())

num_list = [list(map(int, input().split())) for _ in range(n)]
print(num_list)

count = 0


for i in range(n):
    if num_list[i][0] % 2 == (num_list[i][1] + num_list[i][2]) % 2 and num_list[i][0] > num_list[i][1] + num_list[i][2]:
        count += 1


print('YES' if count == n else 'NO')
