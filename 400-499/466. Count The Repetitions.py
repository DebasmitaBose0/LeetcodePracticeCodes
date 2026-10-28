class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # dict to store {s2_index: (s1_count, s2_count)}
        recall = {}
        s1_count, s2_count, s2_idx = 0, 0, 0
        
        while s1_count < n1:
            s1_count += 1
            for char in s1:
                if char == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_count += 1
                        s2_idx = 0
            
            # Check if we have seen this s2_idx at the end of an s1 block before
            if s2_idx in recall:
                prev_s1_count, prev_s2_count = recall[s2_idx]
                
                # Length of the cycle in terms of s1 blocks and s2 matches
                cycle_s1 = s1_count - prev_s1_count
                cycle_s2 = s2_count - prev_s2_count
                
                # Calculate how many full cycles fit in the remaining n1
                num_cycles = (n1 - s1_count) // cycle_s1
                
                # Fast-forward counts
                s1_count += num_cycles * cycle_s1
                s2_count += num_cycles * cycle_s2
                # We don't need to check recall anymore since we skip to the end
                recall = {} 
            else:
                recall[s2_idx] = (s1_count, s2_count)
                
        return s2_count // n2