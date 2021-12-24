class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        if len(needle) > len(haystack): return -1
        
        # The logic is similar to above approach with a very slight improvement. 
        # Instead of only checking chars of needle from left to right, we simultaneously
        # check left to right and right to left so that we can avoid strings which
        # match with needle from start and not match near the end.
        for i in range(len(haystack)):
            start = 0
            # We set end to -1 if len(needle) + i exceeds the len(haystack).
            # Why because, we anyways can't find that needle in substring starting
            # from i, since haystack doesn't have required number of chars for needle
            end = len(needle) - 1 if len(needle) - 1 + i < len(haystack) else -1
            if end == -1: break
            while start <= end:
                # Checking left char
                if haystack[start + i] != needle[start]: break
                # Checking right char
                if haystack[end + i] != needle[end]: break
                start += 1
                end -= 1
            else: return i
        
        return -1