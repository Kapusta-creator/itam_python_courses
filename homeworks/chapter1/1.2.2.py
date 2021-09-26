n = int(input())
false = "False"
true = "True"
in_class = 0
out_of_class = 0
hz_kto = 0
for i in range(n):
    line = input().split()
    kf = 0
    kt = 0
    for j in line:
        if j == false:
            kf += 1
        elif j == true:
            kt += 1
    if kf + kt >= 2:
        if line[3] == false:
            out_of_class += 1
        elif line[3] == true:
            in_class += 1
        else:
            hz_kto += 1
    elif kf:
        out_of_class += 1
    elif kt:
        in_class += 1
    else:
        hz_kto += 1
print(in_class, out_of_class, hz_kto, sep=" ")
