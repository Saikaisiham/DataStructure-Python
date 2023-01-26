from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        print(res)
        stack = []
        for i , t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT,stackI = stack.pop()
                res[stackI] = (i-stackI)
            stack.append([t,i])
        return res

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))