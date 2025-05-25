l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

s = 0
t = 0

for i in l1:
    s += i

for i in l2:
    t += i
    
if s > t:
    print(s)
else:
    print(t)