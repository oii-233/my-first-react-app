t = int(input())
for _ in range(t):
    n = input().strip()
    round_numbers = []
    length = len(n)
    for i, digit in enumerate(n):
        if digit != '0':
            zeros = length - i - 1
            round_numbers.append(int(digit) * (10 ** zeros))
    print(len(round_numbers))
    print(*round_numbers)
