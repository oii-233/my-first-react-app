t = int(input())
for _ in range(t):
    n = input().strip()
    result = []
    length = len(n)
    
    # collect round numbers
    for i in range(length):
        if n[i] != '0':
            result.append(int(n[i] + '0' * (length - i - 1)))
    
    # move the largest (most significant) to the end
    if len(result) > 1:
        # separate largest
        max_val = result[0]  # most significant digit is first
        rest = result[1:]    # all other round numbers
        result = rest + [max_val]
    
    print(len(result))
    print(*result)
