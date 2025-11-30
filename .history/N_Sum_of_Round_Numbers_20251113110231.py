t = int(input())
for _ in range(t):
    n = input().strip()
    round_numbers = []

    length = len(n)
    # collect all round numbers
    for i in range(length):
        if n[i] != '0':
            round_numbers.append(int(n[i] + '0' * (length - i - 1)))

    # separate the largest round number (most significant) to put it last
    if len(round_numbers) > 1:
        max_round = max(round_numbers)
        round_numbers.remove(max_round)
        round_numbers.append(max_round)

    print(len(round_numbers))
    print(*round_numbers)
