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
    t = int(input())
for _ in range(t):
    n = input().strip()
    result = []

    for i in range(len(n)):
        if n[i] != '0':
            # create the round number
            round_num = int(n[i] + '0' * (len(n) - i - 1))
            result.append(round_num)

    # move the largest round number to the end
    if len(result) > 1:
        max_val = max(result)
        result.remove(max_val)
        result.append(max_val)

    print(len(result))
    print(*result)

    print(len(result))
    print(*result)
