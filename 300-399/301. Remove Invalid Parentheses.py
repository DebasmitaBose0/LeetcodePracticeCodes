class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS approach
        queue = {s}  # Use a set to handle unique strings at each level
        while queue:
            # Check if any valid strings exist at the current level
            valid_level = list(filter(isValid, queue))
            if valid_level:
                return valid_level
            
            # Generate the next level by removing one parenthesis
            next_queue = set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':
                        # Form a new string by skipping the character at index i
                        next_queue.add(string[:i] + string[i+1:])
            queue = next_queue
            
        return [""]