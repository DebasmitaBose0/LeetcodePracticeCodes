from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        # Queue stores (current_gene, number_of_mutations)
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            current_gene, steps = queue.popleft()
            
            if current_gene == endGene:
                return steps
            
            # Try mutating each of the 8 positions
            for i in range(len(current_gene)):
                for char in "ACGT":
                    if char != current_gene[i]:
                        mutation = current_gene[:i] + char + current_gene[i+1:]
                        
                        if mutation in bank_set and mutation not in visited:
                            visited.add(mutation)
                            queue.append((mutation, steps + 1))
                            
        return -1