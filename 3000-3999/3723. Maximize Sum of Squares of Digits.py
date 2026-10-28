class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is out of the possible range [1, 9 * num]
        if sum < 1 or sum > 9 * num:
            return ""
            
        res = []
        for i in range(num):
            # Take as much as possible for the current position, 
            # leaving enough sum for the remaining positions if necessary,
            # but since we want the maximum score, greedily take min(9, remaining_sum).
            # Wait, to maximize the score, we want larger digits on the left.
            # Taking min(9, sum - (num - 1 - i) * 9) ensures we don't leave too much or too little,
            # but actually, taking min(9, sum) greedily works because larger digits on the left 
            # naturally maximize both the number value and the sum of squares!
            cur = min(9, sum)
            res.append(str(cur))
            sum -= cur
            
        if sum > 0:
            return ""
            
        return "".join(res)