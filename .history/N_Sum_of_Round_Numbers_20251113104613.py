t = int(input())
for _ in range(t):
    n = input().strip()
    result = []
    length = len(n)
    for i in range(length-1, -1, -1):  
        if n[i] != '0':
            result.append(int(n[i] + '0' * (length - i - 1)))
    print(len(result))
    print(*result)
