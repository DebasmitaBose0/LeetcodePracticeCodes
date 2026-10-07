from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
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

        if not s:
            return [""]

        queue = deque([s])
        visited = {s}
        res = []
        found = False

        while queue:
            level_size = len(queue)
            current_level_res = []

            for _ in range(level_size):
                curr = queue.popleft()

                if isValid(curr):
                    current_level_res.append(curr)
                    found = True

            # If we found valid strings at this level, no need to go deeper
            if found:
                return list(set(current_level_res))

            # Generate next level by removing one parenthesis at each position
            for curr in queue: # Wait, iterate through all elements of the current level before popping them all
                pass
            
            # Proper BFS level processing:
        
        # Let's write the clean standard BFS loop below:
    
    def removeInvalidParentheses(self, s: str) -> list[str]:
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

        if not s:
            return [""]

        queue = deque([s])
        visited = {s}
        found = False
        res = []

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                res.append(curr)
                found = True

            # If a valid string is found, we only continue checking 
            # other strings at the exact same depth level.
            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return list(set(res))