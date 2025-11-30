t= int(input())
for _ in range(t):
    s=str(map(int, input().split()))
    target= "abc"
    count = 0
    for i in range(len(s)):
        if target[i]== s[i]:
            count+=1
    if count>0:
        print("YES")
    else:
        print("NO")
        