t= int(input())
for _ in range(t):
    a,b,c= map(int, input().split())
    for i in(a,b,c):
        if i!=max(a,b,c) and i!=min(a,b,c):
            print(i)
            break