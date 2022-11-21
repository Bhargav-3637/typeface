n=int(input())
l=[0,1,2,5,6,8,9]
c=0
for i in range(1,99999):
    s=str(i)
    for j in s:
        if int(j) not in l:
            break
    else:
        c+=1
        if c==n:
            print(i)
            break
