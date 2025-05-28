 #2743
# n = input()
# print(len(n))

#27866
# s = input()
# n = int(input())
# print(s[n-1])

#9086
# t = int(input())
# for i in range(t):
#     a = input()
#     print(a[0] + a[-1])

#2475
# l = list(map(int,input().split()))
# sum = 0
# for i in l:
#     sum += i*i
# print(sum%10)

#10757
# a, b = map(int,input().split())
# print(a+b)

#2420
# n, m = map(int,input().split())
# print(abs(n-m))

#2744
# print(input().swapcase())

#4101
# while True:
#     a, b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     elif a > b:
#         print('Yes')
#     else:
#         print('No')

#27323
# a = int(input())
# b = int(input())
# print(a*b)

#1271
# n, m = map(int,input().split())
# print(n//m)
# print(n%m)

#15964
# a, b = map(int,input().split())
# print((a+b)*(a-b))

#1264

# s = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# while True:
#     cnt = 0
#     sen = input()
#     if sen == '#':
#         break
#     for i in sen:
#         if i in s:
#             cnt+=1
#     print(cnt)

#2083
# while True:
#     name, age, wht = input().split()
#     age = int(age)
#     wht = int(wht)
    
#     if name == '#' and age == 0 and wht == 0:
#         break
#     if age > 17 or wht >= 80:
#         print(name, 'Senior')
#     else:
#         print(name, 'Junior')

#2440
# n = int(input())
# for i in range(n, 0, -1):
#     print('*' * i)

#2530
# H, M, S = map(int, input().split())
# D = int(input()) 

# S += D % 60
# D = D // 60
# if S >= 60:
#     S -= 60
#     M += 1

# M += D % 60
# D = D // 60
# if M >= 60:
#     M -= 60
#     H += 1

# H += D % 24
# if H >= 24:
#     H -= 24

# print(H,M,S)

#2742
# n = int(input())
# for i in range(n, 0,-1):
#     print(i)

#2752
# n = list(map(int, input().split())) 
# n.sort()  
# print(' '.join(map(str, n))) 

#2845
# L, P = map(int, input().split())
# news = list(map(int, input().split()))
# for i in news:
#     print(i - L * P, end = ' ')

#3046
# r1, s = map(int,input().split())
# print((s*2)-r1)

#4470
# n = int(inpu
# t())
# for i in range(n):
#     s = input()
#     print(f"{i+1}. {s}")

#5524
# n = int(input())
# for i in range(n):
#     s = input()
#     ans = s.lower()
#     print(ans)
    