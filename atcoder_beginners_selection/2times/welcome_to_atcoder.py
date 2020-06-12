#input  a
a = int(input())
#input b c
b,c = map(int, input().split())
#input s
s = str(input())

print('{0} {1}'.format(a+b+c, s))