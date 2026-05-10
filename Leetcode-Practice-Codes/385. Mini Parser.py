# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not None, initializes a default 1integer with a single integer.
#        Otherwise initializes an empty nested list.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a item to it.
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer.
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        
        # Case 1: The input is just a single integer (no brackets)
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num_str = ""
        
        for i, char in enumerate(s):
            if char == '[':
                # Start a new nested list and push it onto the stack
                stack.append(NestedInteger())
            elif char == '-':
                num_str += char
            elif char.isdigit():
                num_str += char
            elif char == ',' or char == ']':
                # If we were building a number, finish it and add it to the current list
                if num_str:
                    stack[-1].add(NestedInteger(int(num_str)))
                    num_str = ""
                
                # If we are closing a list and there is a parent list, add current to parent
                if char == ']' and len(stack) > 1:
                    completed_list = stack.pop()
                    stack[-1].add(completed_list)
        
        return stack[0]