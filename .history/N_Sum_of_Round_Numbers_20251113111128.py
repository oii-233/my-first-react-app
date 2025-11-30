t = int(input())
for _ in range(t):
    n = input().strip()
    round_numbers = []
    length = len(n)
    for i, digit in enumerate(n):
        if digit != '0':
            zeros = length - i - 1
            round_numbers.append(int(digit) * (10 ** zeros))
    
    # Now print them in the same order as example (left to right)
    print(len(round_numbers))
    print(*round_numbers)
