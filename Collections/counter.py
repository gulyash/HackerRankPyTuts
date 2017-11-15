from collections import Counter
input()
shoes = Counter(map(int, input().split()))
n = int(input())
s = 0
for i in range(n):
    shoe_size, xi = map(int, input().split())
    if shoes[shoe_size] != 0:
        shoes[shoe_size] -= 1
        s += xi
print(s)
