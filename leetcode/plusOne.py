class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l=len(digits)
        digits[l-1]=digits[l-1]+1
        for i in range(1,l):
            if digits[l-i]==10:
                digits[l-i]=digits[l-i]-10
                i=i+1
                digits[l-i]=digits[l-i]+1
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)    
        return digits

di=[9,9,9,9,9,9,9]
di2=Solution.plusOne(self=Solution,digits=di)
print(di2)