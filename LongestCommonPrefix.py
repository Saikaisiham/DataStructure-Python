from typing import List

class Solution:
    """
    This code defines a class "Solution" with a method "longestCommonPrefix" that takes in a list 
    of strings as input (strs) and returns the longest common prefix among all the strings in the list. 
    The method first initializes an empty string "res" and then uses nested for loops to iterate through 
    each character of the first string in the list (strs[0]). For each iteration, it compares the character
    at that index in the first string with the same index in all other strings in the list. If the character 
    at that index is not the same in all strings or if the index exceeds the length of any of the other strings, 
    the method returns the "res" string as the longest common prefix. If all characters are the same at that index, it appends the character to the "res" string and continues to the next index.
    If the loop completes without finding any mismatched characters, 
    the method will return the "res" string as the longest common prefix
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        #a b c return empty res cuz theres no common prefix
        for i in range(len(strs[0])):
            # start with first string in strings 
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
            
                    return res

            res += strs[0][i]
        return res


s = Solution()
strs = ['flower','flow','flight']
print(s.longestCommonPrefix(strs))
            