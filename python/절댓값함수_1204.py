n = float(input('실수를 입력하시오.:'))

def abs(n):
    if n < 0:
        return -n
    else:
        return n

print(f'{n}의 절댓값은 {abs(n)}입니다.')
