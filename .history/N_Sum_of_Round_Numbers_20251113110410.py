t = int(input())
for _ in range(t):
    n = input().strip()
    result = []

    # iterate from left to right to collect round numbers
    for i in range(len(n)):
        if n[i] != '0':
            result.append(int(n[i] + '0' * (len(n) - i - 1)))

    # move the largest round number to the end
    if len(result) > 1:
        largest = max(result)
        result.remove(largest)
        result.append(largest)

    print(len(result))
    print(*result)
