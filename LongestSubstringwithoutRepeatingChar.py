class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in Set : 
                Set.remove(s[l])
                l += 1

            Set.add(s[r])
            res = max(res,r-l+1)
        return res

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) 



"""This code defines a class Solution with a method lengthOfLongestSubstring that takes a string s as input and returns the length of the longest substring without repeating characters.

The method uses two pointers, l and r, to keep track of the start and end indices of the current substring. It also uses a set Set to store the characters in the current substring and keep track of repeating characters.

The code starts by initializing the set Set, the start pointer l to 0, and a variable res to store the length of the longest substring.

It then uses a for loop to iterate through the characters in the string from left to right using the end pointer r. For each iteration, the code checks if the current character s[r] is in the set Set. If it is, the code removes the character at the start pointer s[l] from the set and increments the start pointer l until s[r] is not in the set.

The code then adds the current character s[r] to the set Set and updates res to the maximum between res and the length of the current substring r - l + 1.

After the loop completes, the method returns res, which is the length of the longest substring without repeating characters. In the example, the method returns 3 for the input "abcabcbb".
"""
