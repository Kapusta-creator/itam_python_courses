line = input().split(".")[0]
up = 0
interval = 0
for i in range(len(line)):
    if line[i].isupper():
        up = i
        break
for i in range(up, len(line)):
    if line[i].isdigit():
        interval = i + 1
        break
interval -= up
for i in line[up::interval]:
    print(i, sep="", end="")
print(end=".")
