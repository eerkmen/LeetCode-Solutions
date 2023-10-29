#design stack class that support 4 operations
#main problem is to retrieve min element in O(1)
#stack normally normally doesn't support this function

#brute force
#look through entire stack to find the min element
#time complexity: O(n)

#stack
#for each position in the original stack have a corresponding min value as a stack
#ex: original stack: -2,0,-3   min stack: -2,-2,-3
#if -3 popped also pop from the min stack
#time complexity: O(1)
#space complexity: O(n) => actually O(2n) but constant is removed

class MinStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()