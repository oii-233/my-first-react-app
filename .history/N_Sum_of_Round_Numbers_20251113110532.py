t = int(input())
for _ in range(t):
    n = int(input())
    round_numbers = []
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * multiplier)
        n //= 10
        multiplier *= 10

    print(len(round_numbers))
    print(" ".join(map(str, round_numbers)))
