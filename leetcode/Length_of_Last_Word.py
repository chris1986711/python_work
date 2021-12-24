"""Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6."""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=len(s)
        if l==0:
            return 0
        list_s=s.split()
        ls=len(list_s)-1
        ans1=len(list_s[ls])
        return ans1



a="i am luffly"
ans=Solution.lengthOfLastWord(self=Solution,s=a)
print(ans)