# 10872
# n = int(input())
# ans = 1
# for i in range(1, n):
#     ans = ans*i
# if n == 0:
#     print(1)
# else:
#     print(ans*n)

#1075
# l = int(input())
# b = int(input())
# a = int(input())
# c = int(input())
# d = int(input())

# kr = (a + c - 1) // c  # 올림 나눗셈
# mt = (b + d - 1) // d  
# ans = l - max(kr, mt)
# print(ans)

#1173

# N, m, M, T, R = map(int, input().split())

# time = 0
# now = m
# if m + T > M :
#   print(-1)
# else:
#   while True:
#     if N == 0:
#       break
#     if now + T <= M:
#       now += T
#       N -= 1
#     elif now - R < m:
#       now = m
#     elif now - R >= m:
#       now -= R

#     time += 1

#   print(time)

#1212
# print(bin(int(input(), 8))[2:])

#1225
# a, b = input().split()
# a, b = list(map(int,a)), list(map(int,b))
# print(sum(a) * sum(b))

#1233
# s1, s2, s3 = map(int,input().split())
# result = [0]*81
# for i in range(1, s1+1):
#     for j in range(1, s2+1):
#         for q in range(1, s3+1):
#             result[i+j+q] += 1
# print(result.index(max(result)))

#1252
# a, b = input().split()
# print(bin(int(a, 2) + int(b, 2)) [2:])

#2675
# t = int(input())
# for _ in range(t):
#     a, b = input().split()
#     a = int(a)
#     for i in b:
#         print(i*a,end = '')
#     print()

#11720
# t = int(input())
# l = list(map(int,input()))
# sum = 0
# for i in l:
#     sum += i
# print(sum)

#2577
# a = int(input())
# b = int(input())
# c = int(input())

# result = a*b*c
# l = [0] * 10

# for digit in str(result):
#     l[int(digit)] += 1

# for count in l:
#     print(count)

#2920
# scale = list(map(int,input().split()))

# if scale == sorted(scale):
#     print("ascending")
# elif scale == sorted(scale, reverse = True):
#     print("descending")
# else:
#     print('mixed')

#8958
# t = int(input())

# for i in range(t):
#     list = input()
#     score = 0
#     sum = 0
#     for i in list:
#         if i != 'X':
#             sum += 1
#             score += sum
#         else:
#             sum = 0
#     print(score)

#31403
# a = input()
# b = input()
# c = input()

# sum = int(a) + int(b) - int(c)
# print(sum)
# sum1 = int(a+b) - int(c)
# print(sum1)

#10809
# S = input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in S:
#         print(S.index(i), end= ' ')
#     else:
#         print( -1, end =' ')

#10250
# num = int(input())

# for i in range(num):
#     h, w, n = map(int,input().split())
#     floor = n % h
#     room = n // h + 1
#     if floor == 0:
#         room -= 1
#         floor = h
        
#     print(floor*100 + room)
    
    
#1978
# n = int(input())
# data = list(map(int, input().split()))
# count = 0

# for x in data:
#   for i in range(2, x+1):
#     if x % i == 0:
#       if x == i:
#         count += 1
      
#       break

# print(count)
    
#2231

