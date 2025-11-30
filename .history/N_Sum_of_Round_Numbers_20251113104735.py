t = int(input())
for _ in range(t):
    n = input().strip()
    result = []
    length = len(n)
    for i in range(length):
        if n[i] != '0':
            result.append(int(n[i] + '0' * (length - i - 1)))
    
    if len(result) > 1:
        result.sort()
        result.append(result.pop(result.index(max(result))))
    
    print(len(result))
    print(*result)
