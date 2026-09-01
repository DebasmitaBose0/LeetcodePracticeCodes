from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        litters = []
        start_x, start_y = -1, -1
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_x, start_y = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        full_mask = (1 << num_litters) - 1
        
        # Check if start itself is a litter
        initial_mask = 0
        if (start_x, start_y) in litter_map:
            initial_mask |= (1 << litter_map[(start_x, start_y)])
            
        # BFS Queue stores: (x, y, mask, current_energy, steps)
        queue = deque([(start_x, start_y, initial_mask, energy, 0)])
        
        best_energy = {}
        best_energy[(start_x, start_y, initial_mask)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, mask, curr_e, steps = queue.popleft()
            
            if mask == full_mask:
                return steps
            
            # If current energy is 0 and we are not on 'R', we cannot move from here
            if curr_e == 0 and classroom[x][y] != 'R':
                continue
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check boundaries and obstacles
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    next_e = curr_e - 1
                    
                    next_หนด = mask
                    # Check if we collect litter
                    if classroom[nx][ny] == 'L':
                        litter_idx = litter_map[(nx, ny)]
                        next_mask = mask | (1 << litter_idx)
                    else:
                        next_mask = mask
                        
                    # Check if we hit a reset area
                    final_e = energy if classroom[nx][ny] == 'R' else next_e
                    
                    # If energy dropped below 0, invalid move
                    if final_e < 0:
                        continue
                        
                    state_key = (nx, ny, next_mask)
                    if state_key not in best_energy or final_e > best_energy[state_key]:
                        best_energy[state_key] = final_e
                        queue.append((nx, ny, next_mask, final_e, steps + 1))
                        
        return -1