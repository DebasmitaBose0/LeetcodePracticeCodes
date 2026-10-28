class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Push elements in reverse so the first element is at the top
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        # hasNext() guarantees that the top of the stack is an integer
        return self.stack.pop().getInteger()
            
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            
            # If the top is a list, replace it with its contents in reverse
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
            
        return False