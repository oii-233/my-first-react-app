import sys
from io import StringIO

sys.stdin = StringIO("""5
5009
7
9876
10000
10
""")

t = int(input())
for _ in range(t):
    n = input().strip()
    result = []

    for i in range(len(n)):
        if n[i] != '0':
            round_num = int(n[i] + '0' * (len(n) - i - 1))
            result.append(round_num)

    if len(result) > 1:
        max_val = max(result)
        result.remove(max_val)
        result.append(max_val)

    print(len(result))
    print(*result)
