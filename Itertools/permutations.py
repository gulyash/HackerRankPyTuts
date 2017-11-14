from itertools import permutations

s, k = input().split()
sorted_str = ''.join(sorted(s))
perms = permutations(sorted_str, int(k))
print(*(''.join(p) for p in perms), sep='\n')
