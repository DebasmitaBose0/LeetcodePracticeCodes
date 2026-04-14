class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1  # We start at 1, so we need to find the (k-1)-th distance
        
        while k > 0:
            steps = self.get_steps(curr, n)
            if steps <= k:
                # Move to the next sibling
                curr += 1
                k -= steps
            else:
                # Move deeper into the current prefix
                curr *= 10
                k -= 1
                
        return curr

    def get_steps(self, curr, n):
        steps = 0
        first = curr
        last = curr
        while first <= n:
            # Add the number of nodes at the current level
            steps += min(n, last) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps