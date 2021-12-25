class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x==1:
            return 1
        if x==2:
            return 1
        i=2
        
        for i in range(1,x):
            if i*i<x:
                i=i+1
            elif i*i==x:
                return i
            elif i*i>x:
                return i-1