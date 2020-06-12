# s = str(input())
#
# text = ['dream', 'dreamer', 'erase', 'eraser']
#
# for i in range(len(text)):
#     if text[i] in s:
#         cut_string = s.split(text[i])
#         for j in range(len(text)):
#             print(cut_string)
#             if cut_string[j] in text[j]:
#                 print('YES')
#                 exit()
#             else:
#                 break
# print('NO')


s = input()

def solve(query):
    while 1:
        for flag in ("erase", "eraser", "dream", "dreamer"):
            if query.endswith(flag):
                query = query[:-len(flag)]
                break
        else:
            print("NO")
            exit()
        if not query:
            print("YES")
            break

solve(s)