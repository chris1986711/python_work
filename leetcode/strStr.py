class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return (0)
        h_list=list(haystack)
        n_list=list(needle)
        k=len(h_list)-1
        l=len(n_list)-1
        i=0
        j=0
        star=0
        while i<=k and j<=l:
            if h_list[i]==n_list[j]:
                if j==l:
                    return star
                i=i+1
                j=j+1
            else:
                star=star+1
                i=star
                j=0
        return -1


x=Solution.strStr(self=Solution,haystack="mississippi",needle="issip")
print(x)