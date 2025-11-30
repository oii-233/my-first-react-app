t=int(input())
count=0
for _ in range(t):
    sum=0
    nums=input()
    for i in nums:
        sum+=i
    if sum>1:
        count+=1
print(count)
