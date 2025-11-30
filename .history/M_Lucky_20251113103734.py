t = int(input())
for _ in range(t):
    s= list(input())
    first=0
    last=0
    for i in range(3):
        first+=int(s[i])
    for j in range(3,6):
        last+=int(s[j])
    if last==first:
        print("YES")
    else:
        print("NO")