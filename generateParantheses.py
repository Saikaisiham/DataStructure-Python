class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        stack = []
        res = []

        def RecurFunction(opened,closed):
            if opened == closed == n :
                res.append("".join(stack))
            if opened < n:
                stack.append('(')
                RecurFunction(opened+1,closed)
                stack.pop()
            if closed < opened :
                stack.append(')')
                RecurFunction(opened,closed+1)
                stack.pop()

        RecurFunction(0,0)
        return res

        """
        This code defines a class "Solution" with a method "generateParenthesis" that takes in an integer "n" and 
        returns a list of strings. The method uses a stack and a result list to generate all valid combinations of n 
        pairs of parentheses using a recursive function "RecurFunction". The function takes in two parameters, 
        "opened" and "closed" which represent the number of opened and closed parentheses in the current combination. The function checks if the number of opened and closed parentheses is equal to "n" and if so, it adds the current combination to the result list. The function then checks if the number of opened parentheses is less than "n" and if so, it appends an open parenthesis to the stack, calls the recursive function with the opened count incremented by 1, and then pops the last element from the stack. The function also checks if the number of closed parentheses is less than the number of opened parentheses and if so, it appends a closed parenthesis to the stack, calls the recursive function with the closed count incremented by 1, and then pops the last element from the stack. Finally, 
        the method returns the result list containing all valid combinations of n pairs of parentheses.
        """