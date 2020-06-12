# #
# num = []
# n, a, b = map(int, input().split())
#
# for i in range(n+1):
#     if a <= i and i <= b:
#         i_str = str(i)
#         i_length = len(i_str)
#         i_sum = 0
#
#         for j in range(i_length):
#             i_sum += int(i_str[j])
#
#         if a <= i_sum <= b:
#             #numリストに追加
#             num.append(i_sum)
#         else:
#             continue
#     else:
#         continue
#
# print(num)
#
n, a, b = map(int, input().split())
ans = 0
for i in range(n+1):
    if a <= sum(list(map(int, list(str(i))))) <= b:
        ans += i
print(ans)