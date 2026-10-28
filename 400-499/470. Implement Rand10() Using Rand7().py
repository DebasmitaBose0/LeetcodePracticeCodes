# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self) -> int:
        while True:
            # Generate a number between 1 and 49
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            
            # If the index is within the first 40 numbers, we can use it
            if idx <= 40:
                return (idx - 1) % 10 + 1
            
            # Otherwise, 'reject' and loop again