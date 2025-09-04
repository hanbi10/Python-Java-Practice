f = open('data_1.txt', 'r')

lines = f.readlines()
print(lines)

for line in lines:
    print(line)

f.close()