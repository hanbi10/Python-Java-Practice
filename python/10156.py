k, n, m = map(int,input().split())

total = k * n

ans = total - m
if ans < 0:
    print(0)
else:
    print(total - m)