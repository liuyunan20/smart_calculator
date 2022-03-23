n = int(input())
queue = []
out = []
for _ in range(n):
    operation = input().split()
    if operation[0] == "READY":
        queue.append(operation[1])
    elif operation[0] == "EXTRA" and queue:
        name = queue.pop(0)
        queue.append(name)
    elif operation[0] == "PASSED" and queue:
        out.append(queue.pop(0))
print(*out, sep="\n")
