t=int(input())
for _ in range(t):
    num=int(input())
    word=input()
    adi="Timru"
    if num==5 and sorted(word)==sorted(adi):
        print("YES")
    else:
        print("NO")
      