matrix = []


for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

n = 5
sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += matrix[i][i]
    sum2 += matrix[i][n - 1 - i]

if sum1 == sum2:
	print(sum1)
else:
	print(sum1)
	print(sum2)
