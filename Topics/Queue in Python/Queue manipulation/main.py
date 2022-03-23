n = int(input())
queue = []
for _ in range(n):
    operation = input().split()
    if operation[0] == "ENQUEUE":
        queue.append(operation[1])
    elif operation[0] == "DEQUEUE" and queue:
        queue.pop(0)
print(*queue, sep="\n")
