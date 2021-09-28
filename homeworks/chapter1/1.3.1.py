n = int(input())
data = [[] for i in range(n)]
answer = [0 for i in range(n)]
tasks = [False for i in range(n + 1)]
examples = {}
for i in range(n):
    line = list(map(str, input().split()))
    line.append(i)
    if line[2] == line[3]:
        if "1" in examples:
            examples["1"].append(line)
        else:
            examples["1"] = [line]
        tasks[1] = True
    elif line[2] > line[3]:
        if examples.get(line[2]):
            examples[line[2]].append(line)
        else:
            examples[line[2]] = [line]
        tasks[int(line[2])] = True
    else:
        if examples.get(str(round((int(line[2]) + int(line[3])) / 2))):
            examples[str(round((int(line[2]) + int(line[3])) / 2))].append(line)
        else:
            examples[str(round((int(line[2]) + int(line[3])) / 2))] = [line]
        tasks[round((int(line[2]) + int(line[3])) / 2)] = True
for i in range(n, 0, -1):
    if not tasks[i]:
        continue
    students = sorted(examples[str(i)], key=lambda x: (x[0] + x[1], x[4]), reverse=True)
    answer[int(students[0][-1])] = i
    if len(students) > 1:
        for j in range(1, len(students)):
            if "1" in examples:
                examples["1"].append(students[j])
            else:
                examples["1"] = [students[j]]
for i in range(n):
    print(answer[i] + 1, end=" ")
