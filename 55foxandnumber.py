n=int(input())
mat=list(map(int,input().split()))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
k=gcd(mat[0],mat[1])
for i in range(2,len(mat)):
    k=gcd(k,mat[i])
print(k*n)


n=int(input())
mat=list(map(int,input().split()))
help=set(mat)
while len(help)!=1:
    mat.sort(reverse=True)
    if mat[1]!=0:
        c=min(mat)
        mat[0]-=mat[1]
        if mat[0]==0:
            mat[0]=c
    else:
        break
    help=set(mat)
print(sum(mat))
    