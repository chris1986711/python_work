class Solution:
    def climbStairs(self, n: int) -> int:
        list_stairs=[1,2]
        if n==1:
            return 1
        if n==2:
            return 2
        i=2
        k=0
        for i in range(2,n):
            k=list_stairs[i-2]+list_stairs[i-1]
            list_stairs.append(k)
            i=i+1
        return list_stairs[n-1]

s=10
ans=Solution.climbStairs(self=Solution,n=s)
print(ans)