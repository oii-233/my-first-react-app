t= int (input())
for _ in range(t):
    s= list(input())
    count=0
    for i in range(1,len(s)):
        if s[i] > s[0]:
            count+=1
    print(count)