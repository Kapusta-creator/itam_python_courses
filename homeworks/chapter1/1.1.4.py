mas = list(map(int, input().split()))
km = 0
k2 = 0
k8 = 0
for i in mas:
    if i < 0:
        km += 1
    elif i > 8:
        k8 += 1
    if i % 2 == 0:
        k2 += 1
print(km, k8, k2)
