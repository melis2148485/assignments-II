'''Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m
months.'''
n=6
m=3
def fib(n,m):
    if n==1:
        return 1
    dp=[0]*m
    dp[0]=1
    for i in range(2,n+1):
        new_pair=sum(dp[1:])
        for j in range(m-1,0,-1):
            dp[j]=dp[j-1]
        dp[0]=new_pair
    tot_pair=sum(dp)
    return tot_pair
print(fib(n,m))