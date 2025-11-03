n = int(input())
students = []

for _ in range(n):
    row = input().split()
    name = row[0]
    scores = list(map(int, row[1:]))  
    students.append([name] + scores)


students.sort(key=lambda x: x[1], reverse=True)

print(students)
