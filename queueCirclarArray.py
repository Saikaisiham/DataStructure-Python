max_size = None
class Queue : 
    def __init__(self, size=100):
        if size <= 0:
            max_size = 100
        else:
            max_size = size
        
        self.front = 0
        self.arr = [0] * max_size
        self.rear = max_size - 1
        self.count = 0
    

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == max_size

    def enqueue(self,ele) : 
        if self.isFull():
            print('the queue full cant enqueue...!')
        else : 
            self.rear = (self.rear + 1) % max_size
            self.arr[self.rear] = ele
            self.count += 1

    def dequeue(self):
        if self.isEmpty(self):
            print('queue empty cant dequeue...!')
        else : 
            self.front = (self.front + 1) % max_size
            self.count -= 1

    # assert keyword  test if a condition in  code returns True if not the program will raise an AssertionError

    def front_queue(self):
        assert not self.is_empty()
        return self.arr[self.front]
    
    def rear_queue(self):
        assert not self.is_empty()
        return self.arr[self.rear]

    def Display(self):
        if not self.isEmpty():
            for i in range(self.front,self.rear):
                print(self.arr[i] , end=' ')
            print(self.arr[self.rear])

    def search(self,ele):
        pos = -1

        if not self.isEmpty():
            for i in range(self.front,delf.rear):
                if self.arr[i] == ele:
                    pos = i 
                    break
            if pos == -1 : 
                if self.arr[self.rear] == ele:
                    pos = self.rear
        else : 
            print('queue is empty ')

        return pos



q = Queue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.Display()

