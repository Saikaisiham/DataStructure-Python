class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while s[i] == ' ' : 
            i -= 1
        while i>=0 and s[i] != 0 : 
            length += 1
        i -= 1
        return length


s= Solution()
print(s.lengthOfLastWord(' Hello World ')) 