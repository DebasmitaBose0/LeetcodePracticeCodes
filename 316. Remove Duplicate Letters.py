class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Store the last index where each character occurs
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            # We only process the character if it's not already in our result
            if char not in visited:
                # If the current char is smaller than the last char in stack
                # AND the last char in stack appears later, we can remove it
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    visited.remove(stack.pop())
                
                stack.append(char)
                visited.add(char)
        
        return "".join(stack)