t=int(input())
count=0
for _ in range(t):
    sum=0
    nums=list(input().split())
    for i in nums:
        sum+=int(i)
    if sum>1:
        count+=1
print(count)
