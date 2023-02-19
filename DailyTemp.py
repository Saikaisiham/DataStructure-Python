from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This line defines a class Solution that contains a method dailyTemperatures which 
        # takes in a list of integers temperatures and returns a list of integers.
        res = [0] * len(temperatures)
        # This line initializes a list res of the same length as the input temperatures, filled with zeros. This list
        #  will store the number of days it will take for each temperature to warm up.
        stack = []
        for i , t in enumerate(temperatures):
            # This line starts a for loop that will iterate over the input temperatures.
            # The enumerate function returns the index i and the value t of each temperature in the list.
            while stack and t> stack[-1][0]:
                # This line starts a while loop that continues as long as stack is not empty and
                # the current temperature t is greater than the temperature stored in the top of the stack.
                stackT,stackI = stack.pop()
                # This line pops the last element from the stack and assigns its value to two variables stackT and stackI.
                # stackT holds the temperature and stackI holds the index of the temperature.
                res[stackI] = (i-stackI)
                # This line calculates the number of days it will take for the popped temperature to warm up by subtracting its index stackI 
                # from the current index i. The result is stored in the res list at the index stackI.
            stack.append([t,i]) 
        return res

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))