f = open('data_2.txt', 'w')

while True:
    content = input('내용 입력:')
    if content == '':
        break
    f.write(content + '\n')

f.close()