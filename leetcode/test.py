class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_list=list(haystack)
        n_list=list(needle)
        k=len(h_list)-1
        l=len(n_list)-1
        i=0
        j=0
        if needle in haystack and n_list !=[]:
            while i<=k:
                if h_list[i]==n_list[j]:
                    while j<=l and i<=k:
                        if h_list[i]==n_list[j]:
                            i=i+1
                            j=j+1
                        elif h_list[i]!=n_list[j]:
                            i=i+1
                            j=0
                    break       
                elif h_list!=n_list[j]:
                    i=i+1
            return(i-len(n_list))
        elif needle in haystack and n_list==[]:
            return (0)
        else: 
            return(-1)


"mississippi"
"issip"
x=Solution.strStr(self=Solution,haystack="mississippi",needle="issip")
print(x)