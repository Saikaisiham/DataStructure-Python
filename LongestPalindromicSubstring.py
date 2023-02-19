class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0

        for i in range(len(s)):
            #odd length 
            l,r = i , i
            while l>=0 and r<len(s) and s[l]== s[r] :
                if (r-l+1) > length : 
                    # The condition (r-l+1) > length checks if the length of the current substring 
                    # represented by the indices l and r is longer than the length of the longest palindromic
                    # substring stored in the length variable. If this condition is true, it means that the current
                    # substring is a longer palindromic substring than the one previously stored in res, so we update
                    # res to be the current substring
                    #  and update length to be the length of the current substring.
                    res = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
                # The pointer r is incremented rather than decremented because we are trying to 
                # extend the current palindromic substring to the right. In other words, we are trying to 
                # find a larger palindromic substring by increasing the size of the substring to the right. 
                # On the other hand, the pointer l is decremented because we are trying to extend the current 
                # palindromic substring to the left. This way, the two pointers l and r move towards each other, 
                # either extending the current palindromic 
                # substring or indicating that the current palindromic substring has reached its maximum size.

            #even length
            l , r = i ,i+1
            while l>=0 and  r < len(s) and s[l] == s[r]:
                if (r-l+1) > length : 
                    res = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
        return res

