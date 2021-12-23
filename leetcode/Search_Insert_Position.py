"""Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums==[]:
            return 0
        if target == nums[0]:
            return 0
        l=len(nums)
        i=0
        for i in range(0,l):
            if nums[i]<target:
                i=i+1
            elif nums[i]>=target:
                return i        
        return i 


input=[1,3]
t=2
ans=Solution.searchInsert(self=Solution,nums=input,target=t)
print(ans)