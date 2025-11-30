t = int(input())
for _ in range(t):
    n = input().strip()
    result = []

    # iterate from least significant to most significant digit
    for i in range(len(n)-1, -1, -1):
        if n[i] != '0':
            round_num = int(n[i] + '0' * (len(n)-i-1))
            result.append(round_num)
    
    # reverse the list so smallest place values first, largest last
    result = result[::-1]

    print(len(result))
    print(*result)
