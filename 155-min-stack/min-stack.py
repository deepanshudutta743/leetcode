class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # newVal = min(val, self.minStack[-1] if self.minStack else val)
        # self.minStack.append(newVal)

    def pop(self) -> None:
        self.stack.pop()
        # self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]       

    def getMin(self) -> int:
        tmp=[]
        mini=self.stack[-1]
        while len(self.stack):
            top=self.stack[-1]
            mini=min(mini,top)
            tmp.append(self.stack.pop())
        while len(tmp):
            self.stack.append(tmp.pop())
        return mini        

        
