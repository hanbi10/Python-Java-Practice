f = open('data_1.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()