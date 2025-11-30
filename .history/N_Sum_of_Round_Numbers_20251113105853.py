t = int(input())
for _ in range(t):
    n = input().strip()
    result = []
    length = len(n)
    
    # iterate from right to left
    for i in range(length - 1, -1, -1):
        if n[i] != '0':
            result.append(int(n[i] + '0' * (length - i - 1)))
    
    # reverse to match the example: smaller values first, largest last
    result = result[::-1]
    
    print(len(result))
    print(*result)
