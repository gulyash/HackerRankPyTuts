from itertools import combinations

input()
s = ''.join(input().split())
k = int(input())
sorted_str = ''.join(sorted(s))
contains_a = 0
combs = list(combinations(sorted_str, k))
for c in combs:
    if 'a' in c:
        contains_a += 1
print('{:.4f}'.format(contains_a/len(combs)))
