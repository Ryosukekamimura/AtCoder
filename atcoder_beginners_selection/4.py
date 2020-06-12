def calc_division(n):
    return n / 2




#input N
N = int(input())

#input A_1, A_2, A_3, ... A_n
s = int(input().split())
count = 0

s_division = map(calc_division, s)
print(s_division)

