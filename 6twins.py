n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
coin=totnow=0
s=sum(arr)
while(totnow<=s//2):
    totnow+=arr[coin]
    coin+=1
print(coin)