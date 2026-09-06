class MinStack:
    def __init__(self):
        self.stack = []
        self.mn = [float('inf')]

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.mn.append(min(self.mn[-1],value))

    def pop(self) -> None:
        self.stack.pop()
        self.mn.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        
    def getMin(self) -> int:
        #print(self.mn[-1])
        return self.mn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()