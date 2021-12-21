class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=len(nums)
        i=0
        for k in range(0,k):
            if nums[k]!= val:
                nums[i]=nums[k]
                i=i+1
        return i

        



elementA=[1,2,3,3,4,4,4,5,5]
s=Solution.removeElement(self=Solution,nums=elementA,val=3)
print(elementA)
print(s)
