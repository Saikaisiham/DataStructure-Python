max_size =5
class stack :
    
    def __init__(self):
        self.top =-1
        self.items = [None]*max_size
    
    
    def isEmpty(self):
        return self.top<0

    def push(self,element):
        if self.top>=max_size-1:
            print('the stack full  on push')
        else :
            self.top +=1
            self.items[self.top]=element
    
    def pop(self):
        if self.isEmpty():
            print('the stack is Empty')
        else:
            self.top-=1

    def getTop(self):
        if self.isEmpty():
            print('the stack is empty')
        else : 
            stack_top = self.items[self.top]
            print(stack_top)

    def displayStack(self):
        print('[',end="")
        for i in range (self.top,-1,-1):
            print(self.items[i], end="")
        print("]")


s = stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.displayStack()


    
            

