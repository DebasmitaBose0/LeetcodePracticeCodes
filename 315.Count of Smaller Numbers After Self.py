class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # We store pairs of (value, original_index) to track counts correctly
        indices = list(range(n))
        
        def merge_sort(left, right):
            if right - left <= 1:
                return indices[left:right]
            
            mid = (left + right) // 2
            l_part = merge_sort(left, mid)
            r_part = merge_sort(mid, right)
            
            merged = []
            l_idx, r_idx = 0, 0
            
            # Merge and count
            while l_idx < len(l_part) and r_idx < len(r_part):
                # If left element is greater than right element, 
                # then all remaining elements in r_part from r_idx onwards
                # are smaller than l_part[l_idx]
                if nums[l_part[l_idx]] > nums[r_part[r_idx]]:
                    # Every element from r_idx to the end of r_part is smaller
                    ans[l_part[l_idx]] += len(r_part) - r_idx
                    merged.append(l_part[l_idx])
                    l_idx += 1
                else:
                    merged.append(r_part[r_idx])
                    r_idx += 1
            
            merged.extend(l_part[l_idx:])
            merged.extend(r_part[r_idx:])
            return merged

        # We sort in descending order to easily count smaller elements to the right
        merge_sort(0, n)
        return ans