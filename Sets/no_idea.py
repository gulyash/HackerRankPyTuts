input()
m = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for c in m:
    if c in a:
        happiness += 1
    if c in b:
        happiness -= 1
print(happiness)
