class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i=0
        j=0
        s=0
        l=len(nums)
        sum_list=[]
        for i in range(0,l):
            s=0
            for j in range(i,l):
                s=s+nums[j]
                sum_list.append(s)
        ans=max(sum_list)
        print(sum_list)
        return ans

a_list=[-2,1,-3,4,-1,2,1,-5,4]
maxS=Solution.maxSubArray(self=Solution,nums=a_list)
print(maxS)