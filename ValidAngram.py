class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False 
        coT,coS = {},{}
        for i in range (len(s)):
            coS[s[i]] = 1+ coS.get(s[i],0)
            coT[t[i]] = 1+ coT.get(t[i],0)
        for c in coS : 
            if coS[c] != coT.get(c,0):
                return False
        return True