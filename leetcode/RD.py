class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


b=[1,1,2,3,3,4,4,5]

a=Solution.removeDuplicates(self=Solution,nums=b)
print(a,b)
