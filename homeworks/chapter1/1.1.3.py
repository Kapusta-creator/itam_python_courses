line = input()
if len(line) >= 6:
    print(line[3], line[5])
    line = line[:3] + line[4] + line[6:]
    print(line)
else:
    line = line[::-1]
    for i in range(0, len(line), 2):
        print(line[i], end=" ")
