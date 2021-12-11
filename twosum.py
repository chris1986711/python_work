nums = [2,7,11,1,4,9,5]
target = 11
i = 0
j = 0
k=len(nums)
while i < k:
    while j < k :
        if nums[i]+nums[j]==target:
            print(i,j)
        j = j+1
    j = i + 1
    i = i + 1        