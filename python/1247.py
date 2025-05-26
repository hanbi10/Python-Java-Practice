import sys
input = sys.stdin.readline #input()으로 받으면 시간초과가 발생 

for _ in range(3) :
    t = int(input())
    hap = 0
    for i in range(t) :
        hap += int(input())
    if hap == 0 :
        print('0')
    elif hap > 0 :
        print('+')
    else :
        print('-')

# sys.stdin.readline() 사용법
# 한개의 정수 = int(sys.stdin.readline()) -> 한줄 단위로 입력 받기 때문에 개행 문자가 같이 입력 받아짐, 또한 str형태로 저장 되기 때문에 형 변환 필요
# 정해진 개수의 정수 = map(int, sys.stdin.readline().split()) -> 공백을 기준으로 입력 받기 때문에 개행 문자가 같이 입력 받아짐
