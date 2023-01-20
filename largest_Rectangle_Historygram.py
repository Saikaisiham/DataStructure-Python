class Solution :
    def Historygram(self,heights:list[int])->list[int]:
        maxArea = 0
        stack=[]#index,height

        for i , h in enumerate(heights):
            start = i 
            while stack and stack[-1][1]>h:
                index,height = stack.pop()

                maxArea = max(maxArea,height*(i-index))

                start = index
            stack.append((start,h))
        
        for i , h in stack : 
            maxArea = max(maxArea,h*(len(height)-i))
        
        return maxArea

