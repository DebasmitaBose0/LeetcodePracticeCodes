
from ast import List
from array import array

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sum
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Next greater element to the right
        nxt = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nxt[stack.pop()] = i
            stack.append(i)

        # Binary lifting tables
        LOG = n.bit_length()

        jump = [array('i', nxt)]
        cost = [array('q', [
            nums[i] * (nxt[i] - i)
            - (pref[nxt[i]] - pref[i])
            for i in range(n)
        ])]

        for j in range(1, LOG):
            prev_jump = jump[-1]
            prev_cost = cost[-1]

            curr_jump = array('i', [n]) * n
            curr_cost = array('q', [0]) * n

            for i in range(n):
                mid = prev_jump[i]

                if mid < n:
                    curr_jump[i] = prev_jump[mid]
                    curr_cost[i] = prev_cost[i] + prev_cost[mid]
                else:
                    curr_cost[i] = prev_cost[i]

            jump.append(curr_jump)
            cost.append(curr_cost)

        # Calculate minimum operations for nums[l:r+1]
        def get_cost(l, r):
            total = 0
            cur = l

            for j in range(LOG - 1, -1, -1):
                nxt_pos = jump[j][cur]

                if nxt_pos <= r:
                    total += cost[j][cur]
                    cur = nxt_pos

            # Remaining partial block
            total += (
                nums[cur] * (r - cur + 1)
                - (pref[r + 1] - pref[cur])
            )

            return total

        # Sliding window
        ans = 0
        l = 0

        for r in range(n):
            while get_cost(l, r) > k:
                l += 1

            ans += r - l + 1

        return ans
