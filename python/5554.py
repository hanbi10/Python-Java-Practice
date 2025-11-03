a = int(input())
b = int(input())
c = int(input())
d = int(input())

sum = a + b + c + d
x = 0
y = 0

if sum >= 0:
    x = sum // 60
    y = sum % 60
else:
    x = 0 
    y = sum

print(x)
print(y)