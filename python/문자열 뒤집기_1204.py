class reversed_str:
    def rev(a):
        a.reverse()
        return a
a = list(input())
print(''.join(reversed_str.rev(a)))