s = input()
array = ['erase', 'dream', 'dreamer', 'eraser']


for i in range(len(array)):
    if s.endswith(array[i]):
        s = s[:-len(array[i])]
        for j in range(len(array)):
            if s.endswith(array[j]) and len(s) == len(array[j]):
                print('YES')
                exit()
            else:
                continue

print('NO')


