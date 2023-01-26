import re


class Solution:
    def longestPalindrome(self, s2: str) -> str:
        def remove(s2):
            return s2.replace(" ", "")
            return s2.remove(',')
        
        s= remove(s2.lower())

        s2=re.sub(",","",s)
        length = 0

        for i in range(len(s2)):
            #odd length 
            l,r = i , i
            while l>=0 and r<len(s2) and s2[l]== s2[r] :
                if (r-l+1) > length : 
                    res = s2[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1

            #even length
            l , r = i ,i+1
            while l>=0 and  r < len(s2) and s2[l] == s2[r]:
                if (r-l+1) > length : 
                    res = s2[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
        return "Palindrome"


s = Solution()
print(s.longestPalindrome("A man, a plan, a canal: Panama"))


