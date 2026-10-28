class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Dictionary to store the frequency of edges at each vertical position
        edge_counts = {}
        
        for row in wall:
            current_pos = 0
            # Iterate through all bricks except the last one in the row
            # (Because we cannot draw a line at the right edge of the wall)
            for i in range(len(row) - 1):
                current_pos += row[i]
                edge_counts[current_pos] = edge_counts.get(current_pos, 0) + 1
        
        # If there are no internal edges, the max frequency is 0
        max_edges = max(edge_counts.values()) if edge_counts else 0
        
        # Minimum bricks crossed = Total rows - Maximum edges aligned
        return len(wall) - max_edges