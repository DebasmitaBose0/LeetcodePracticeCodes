class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # 1. Apply Gravity: Move stones '#' to the rightmost possible position in each row
        for row in boxGrid:
            # We track the 'empty' slot starting from the far right
            empty_slot = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '#':
                    # Move stone to the lowest available empty slot
                    row[col], row[empty_slot] = row[empty_slot], row[col]
                    empty_slot -= 1
                elif row[col] == '*':
                    # Obstacles reset the empty slot position to the left of the obstacle
                    empty_slot = col - 1
        
        # 2. Rotate 90 Degrees Clockwise:
        # A cell at (r, c) moves to (c, m - 1 - r)
        res = [["" for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]
                
        return res