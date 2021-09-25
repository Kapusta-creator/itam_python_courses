mas = list(map(int, input().split()))
minn = mas[0]
maxx = mas[0]
for i in mas:
    if minn > i:
        minn = i
    if maxx < i:
        maxx = i
print(minn, ", ", maxx, sep="")
