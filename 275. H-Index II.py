class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Number of papers with at least citations[mid] citations
            # is (total papers - current index)
            count = n - mid
            
            if citations[mid] == count:
                return count
            elif citations[mid] < count:
                # We need more citations, move right
                left = mid + 1
            else:
                # We have enough citations, but could potentially 
                # find a larger h-index by moving left
                right = mid - 1
                
        # The h-index will be n - left
        return n - left