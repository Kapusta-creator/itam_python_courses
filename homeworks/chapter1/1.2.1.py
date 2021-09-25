n = int(input())
in_class = 0
out_of_class = 0
for i in range(n):
    status = input().split()[-1]
    if status[0] == "F":
        out_of_class += 1
    else:
        in_class += 1
print(in_class, out_of_class)
