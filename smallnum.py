#14praveen

def reduceN(n,k):
    if k<=0: return n
    if n==0: return 10
    p1=reduceN(n//10,k)*10+n%10
    p2=reduceN(n//10,k-1)
    if p1<p2:
        return p1
    else:
        return p2
n,k=input().split()
n,k=int(n),int(k)
print(reduceN(n,k))
