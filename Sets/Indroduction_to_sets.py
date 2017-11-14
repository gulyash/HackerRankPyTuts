_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))
print(*sorted(a.symmetric_difference(b)), sep='\n')
