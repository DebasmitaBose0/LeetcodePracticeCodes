class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            # Check 4 directions: North, South, East, West
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from the top/bottom edges
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])        # Top (Pacific)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Bottom (Atlantic)

        # Start DFS from the left/right edges
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])        # Left (Pacific)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Right (Atlantic)

        # Return coordinates present in both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res