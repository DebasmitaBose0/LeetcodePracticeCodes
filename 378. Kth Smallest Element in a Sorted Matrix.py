class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        def countLessEqual(mid):
            # Efficiently count elements <= mid in O(n)
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += (row + 1)
                    col += 1
                else:
                    row -= 1
            return count

        ans = low
        while low <= high:
            mid = (low + high) // 2
            if countLessEqual(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans