class StackNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    def push(self, new_item):
        new_ptr = StackNode(new_item, self.top_ptr)
        self.top_ptr = new_ptr

    def pop(self):
        if self.is_empty():
            print("Stack empty on pop")
        else:
            temp = self.top_ptr
            self.top_ptr = self.top_ptr.next
            temp.next = None
            del temp

    def pop_and_return(self):
        if self.is_empty():
            print("Stack empty on pop")
            return None
        else:
            stack_top = self.top_ptr.item
            temp = self.top_ptr
            self.top_ptr = self.top_ptr.next
            temp.next = None
            del temp
            return stack_top

    def get_top(self):
        if self.is_empty():
            print("Stack empty on getTop")
        else:
            stack_top = self.top_ptr.item
            print("Top Element of the stack is", stack_top)

    def display(self):
        cur_ptr = self.top_ptr
        print("Items in the stack : [", end=" ")
        while cur_ptr is not None:
            print(cur_ptr.item, end=" ")
            cur_ptr = cur_ptr.next
        print("]")

s = Stack()
s.push(10)
s.push(5)
s.push(8)
s.push(0)
s.push(9)
s.push(13)
s.display()
