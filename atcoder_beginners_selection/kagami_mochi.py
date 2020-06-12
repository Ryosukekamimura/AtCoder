n = int(input())
d = [int(input()) for i in range(n)]


count = 0
new_list = [i for i in d if i != max(d)]
count += 1

while True:

    if len(new_list) != 0:
        new_list = [i for i in new_list if i != max(new_list)]
        count += 1
        continue
    else:
        break


print(count)