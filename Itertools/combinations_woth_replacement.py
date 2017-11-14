from itertools import combinations_with_replacement

s, k = input().split()
sorted_str = ''.join(sorted(s))
combs = combinations_with_replacement(sorted_str, int(k))
print(*(''.join(c) for c in combs), sep='\n')
