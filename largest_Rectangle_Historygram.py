class Solution :
    def Historygram(self,heigths:list[int])->list[int]:
        maxArea = 0
        stack=[]#index,height

        for i , h in enumerate(heigths):
            start = i 
            while stack and stack[-1][1]>h:
                index,heigth = stack.pop()

                maxArea = max(maxArea,heigth*(i-index))

                start = index
            stack.append((start,h))
        
        for i , h in stack : 
            maxArea = max(maxArea,h*(len(heigth)-i))
        
        return maxArea

