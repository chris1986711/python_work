class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_list=list(haystack)
        n_list=list(needle)
        k=len(h_list)-1
        i=0
        if needle in haystack:
            while i<=k:
                if h_list[i]==n_list[0]:
                    break
                elif h_list!=n_list[0]:
                    i=i+1
            return(i)
        else: 
            return(-1)
            
a='a'
b=''
r=Solution.strStr(self=Solution,haystack=a,needle=b)
print(b in a)
print(len(b))
c=list(b)
print(c==[])