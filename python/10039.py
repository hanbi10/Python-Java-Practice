sum = 0

for i in range(5):
    a = int(input())
    if a >= 40:
        sum += a
    else:
        sum += 40
    
print(sum // 5)