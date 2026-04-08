class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        # We track indices to know the original position of each number
        indices = list(range(n))
        
        def merge_sort(left, right):
            if right - left <= 1:
                return
            
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)
            
            temp = []
            i, j = left, mid
            # jump_count tracks how many elements from the right side 
            # are smaller than the current element on the left side
            jump_count = 0 
            
            while i < mid or j < right:
                # If right is exhausted OR (left is not exhausted AND left element <= right element)
                if j == right or (i < mid and nums[indices[i]] <= nums[indices[j]]):
                    # The number of smaller elements to the right of indices[i] 
                    # is the total number of 'j' elements already merged
                    counts[indices[i]] += jump_count
                    temp.append(indices[i])
                    i += 1
                else:
                    # Right element is smaller than left element
                    temp.append(indices[j])
                    j += 1
                    jump_count += 1
            
            indices[left:right] = temp

        merge_sort(0, n)
        return counts