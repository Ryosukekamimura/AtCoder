n = int(input())
a = list(map(int, input().split()))

alice = []
bob = []

for i in range(n):
    max_value = max(a)
    a.remove(max_value)
    if i % 2 == 0:
        alice.append(max_value)
    else:
        bob.append(max_value)

print('{0}'.format(sum(alice) - sum(bob)))