total = int(input())
sum = 0
for i in range(9):
    a = int(input())
    sum += a
ans = total - sum
print(ans)