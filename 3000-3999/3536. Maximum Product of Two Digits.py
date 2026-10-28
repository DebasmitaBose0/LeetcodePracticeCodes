class Solution:

  def maxProduct(self, n: int) -> int:
    # Convert number to a sorted list of integer digits in descending order
    digits = sorted([int(d) for d in str(n)], reverse=True)

    # Return the product of the two largest digits
    return digits[0] * digits[1]