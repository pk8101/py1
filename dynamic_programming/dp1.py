# solving fib using dp
import sys ,math
sys.setrecursionlimit(100000)

def fib(n,dp):
    if n==0 or n==1:
        return n
    if dp[n-1]==-1:
        ans1=fib(n-1,dp)
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]
    if dp[n-2]==-1:
        ans2=fib(n-2,dp)
        dp[n-2]=ans2
    else:
        ans2=dp[n-2]
        
    myans=ans1+ans2
    return myans


def fibI(n):
    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1
    i=2
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    return dp[n]
n=10
dp=[-1 for i in range(n+1)]
ans=fib(n,dp)
ans1=fibI(n)
print(ans1)


#steps from n to 1 using dp and recursion(conditions 1.wher n can divided by two or three 2.n can go to n-1)
def minSteps(n,dp):
    if n==1:
        return 0
    ans1=sys.maxsize
    if n%3==0:
        if dp[n//3]==-1:
            ans1=minSteps(n//3,dp)
            dp[n//3]=ans1
        else:
            ans1=dp[n//3]
    ans2=sys.maxsize
    if n%2==0:
        if dp[n//2]==-1:
            ans2=minSteps(n//2,dp)
            dp[n//2]==ans2
        else:
            ans2=dp[n//2]
    if dp[n-1]==-1:
        ans3=minSteps(n-1,dp)
        dp[n-1]=ans3
    else:
        ans3=dp[n-1]
    ans=1+min(ans1,ans2,ans3)
    return ans


n1=90
dp=[-1 for i in range(n1+1)]
ans3=minSteps(n1,dp)
print(ans3)

# solve minimum squares for N using dp
def minSquares(n,dp):
    if n==0:
        return 0
    
    ans=sys.maxsize
    root=int(math.sqrt(n))
    for i in range(1,root+1):
        newCheck=n-(i**2)
        if dp[newCheck]==-1:
            smallans=minSquares(newCheck,dp)
            dp[newCheck]=smallans
            current=1+smallans
        else:
            current=1+dp[newCheck]
        ans=min(ans,current)
    return ans

n2=41
dp=[-1 for i in range(n2+1)]
ans4=minSquares(n2,dp)
print(ans4)

#min squares problem in iterative solution
def minSquaresI(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    for i in range(1,n+1):
        ans=sys.maxsize
        root=int(math.sqrt(i))
        for j in range(1,root+1):
            curr=1+dp[i-(j**2)]
            ans=min(curr,ans)
        dp[i]=ans
    return dp[n]
n3=41
ans5=minSquaresI(n3)
print(ans5)