class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
    
        i=1
        while i <=x:
            if i*i<x:
                i=i+1
            elif i*i==x:
                return i
            elif i*i>x:
                return i-1
a=4
b=Solution.mySqrt(self=Solution,x=a)                
print(b)
c=a^2
print(c)