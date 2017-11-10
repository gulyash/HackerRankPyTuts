marks = [[input(), float(input())] for _ in range(int(input()))]
grades = sorted({s[1]for s in marks})
result = sorted(s[0] for s in marks if s[1] == grades[1])
print('\n'.join(result))
