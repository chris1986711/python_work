class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix +=x
            else: break
        return prefix