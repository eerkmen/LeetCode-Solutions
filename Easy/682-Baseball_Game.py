#stack data structure
#iterate through all of the operations
#so if else case
#if c pop
#if d top of the stack double it and add to the stack
#if + add previous score and add to the stack
#return all of the values in stack summed
#time complexity: O(n) =>iterating every single input
#space complexity: O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
              stack.append(stack[-1] + stack[-2])
            elif op == "D":
              stack.append(2 * stack[-1])
            elif op == "C":
              stack.pop()
            else:
               stack.append(int(op))

        return sum(stack)