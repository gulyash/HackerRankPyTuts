from collections import deque

for _ in range(int(input())):
    input()
    d = deque(map(int, input().split()))
    lastPicked = max(d[0], d[len(d) - 1])
    d.pop() if d[0] < d[len(d) - 1] else d.popleft()
    for i in range(len(d)):
        m = max(d[0], d[len(d)-1])
        if m > lastPicked:
            print('No')
            break
        else:
            lastPicked = m
            d.pop() if d[0] < d[len(d) - 1] else d.popleft()
    if len(d)==0:
        print('Yes')