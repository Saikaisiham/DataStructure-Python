class Solution:

    """
    Input: n = 4
    Output: "1211"
    Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = say "1" = one 1 = "11"
    countAndSay(3) = say "11" = two 1's = "21"
    countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
    """
    def countAndSay(self, n: int) -> str:

        if n == 1 :
            return "1"

        prev = self.countAndSay(n-1)
        res = ""
        ct = 1

        for i in range(len(prev)):
            if i == len(prev)-1 or prev[i] != prev[i+1]:
                res += str(ct) + prev[i]
                ct = 1
            else :
                ct += 1
        return res









        