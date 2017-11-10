n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
result = sum(student_marks[input()])/3
print('{:.2f}'.format(result))