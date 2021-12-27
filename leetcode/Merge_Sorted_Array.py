class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2==[]:
            return nums1
        if nums1==[0]:
            return nums2
        i=0
        j=0
        
        l1=len(nums1)
        l2=len(nums2)

        l=l1+l2-2

        while i+j<=l:
             
            if nums1[i]<nums2[j]:
                i=i+1
            elif nums1[i]==nums2[j]:
                nums1.insert(i,nums2[j])
                nums1.pop(-1)
                i=i+2
                j=j+1
            elif nums1[i]==0:
                nums1.insert(i,nums2[j])
                nums1.pop(-1)
                i=i+1
                j=j+1
        return nums1          
            
                




n1=[1,2,3,0,0,0]
n2=[2,5,6]
#if i<j
n1.insert(1,n2[0])#(i+1)
n1.pop(-1)
print(n1)
#if i<j
n1.insert(4,n2[1])
n1.pop(-1)
print(n1)
#i=0 j!=0
n1.insert(5,n2[2])
n1.pop(-1)
print(n1)
