t=int(input())
target="codeforces"
for _ in range (t):
    count=0
    s= str(input())
    for i in range(10):
        if target[i]!=s[i]:
            count+=1
    print(count)