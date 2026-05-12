class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in descending order
        citations.sort(reverse=True)
        
        h = 0
        # Iterate through the sorted list
        for i, c in enumerate(citations):
            # If the current citation count is greater than the current rank (i)
            # it means we have at least (i + 1) papers with >= (i + 1) citations
            if c >= i + 1:
                h = i + 1
            else:
                # Since it's sorted, if this condition fails, 
                # no subsequent papers will satisfy it
                break
                
        return h