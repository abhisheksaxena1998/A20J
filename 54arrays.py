n=int(input())
mat=map(int,input().split())
a,b,c=[],[],[]
for i in mat:
    if i<0:
        a.append(i)
    elif i>0:
        b.append(i)
    else:
        c.append(i)
if len(b)==0:
    b.append(a.pop())
    b.append(a.pop())
if len(a)%2==0:
    c.append(a.pop())
print(len(a), *a,sep=" ")
print(len(b), *b,sep=" ")
print(len(c), *c,sep=" ")