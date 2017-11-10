n = input()
l = list(map(int, input().split()))
l = list(filter(lambda a: a != max(l), l))
print(max(l))
