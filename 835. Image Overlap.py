from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Collect coordinates of all 1s in both images
        transition1 = [(r, c) for r in range(len(img1)) for c in range(len(img1[0])) if img1[r][c] == 1]
        transition2 = [(r, c) for r in range(len(img2)) for c in range(len(img2[0])) if img2[r][c] == 1]
        
        # Count the frequency of each translation vector
        vector_counts = Counter(
            (r2 - r1, c2 - c1) 
            for r1, c1 in transition1 
            for r2, c2 in transition2
        )
        
        # Return the maximum overlap count (if both are empty, vector_counts will be empty, so return 0)
        return max(vector_counts.values()) if vector_counts else 0