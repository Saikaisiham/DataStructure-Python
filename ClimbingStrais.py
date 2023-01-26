class Solution:
    def climbStairs(self, n: int) -> int:

        """ in this algo gonna use DP """

        one , two = 1,1

        for i in range(n-1):
            temp = one
            one = one  + two 
            two = temp
        return one

s = Solution()
print(s.climbStairs(5))