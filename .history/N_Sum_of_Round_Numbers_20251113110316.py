t = int(input())
for _ in range(t):
    n = input().strip()
    result = []

    for i in range(len(n)):
        if n[i] != '0':
            result.append(int(n[i] + '0' * (len(n)-i-1)))

    if len(result) > 1:
        # move the largest round number to the end
        max_val = max(result)
        result.remove(max_val)
        result.append(max_val)

    print(len(result))
    print(*result)
