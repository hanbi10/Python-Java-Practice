f = open('data_1.txt', 'a')

for i in range(11, 21):
    line = f"{i}번째 줄입니다.\n"
    f.write(line)
    
f.close()