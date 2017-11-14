from itertools import combinations

s, k = input().split()
sorted_str = ''.join(sorted(s))
for i in range(1, int(k) + 1):
    print(*(''.join(c) for c in combinations(sorted_str, i)), sep='\n')

