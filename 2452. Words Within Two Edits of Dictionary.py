class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []
        
        for query in queries:
            for word in dictionary:
                edits = 0
                for i in range(n):
                    if query[i] != word[i]:
                        edits += 1
                    # Optimization: if we exceed 2, this word is invalid
                    if edits > 2:
                        break 
                
                # If we found a dictionary word within 2 edits
                if edits <= 2:
                    res.append(query)
                    break # Move to the next query immediately
                    
        return res