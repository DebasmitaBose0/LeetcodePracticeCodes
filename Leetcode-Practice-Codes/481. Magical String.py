class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0: return 0
        if n <= 3: return 1 # s is "122...", first 3 chars have one '1'
        
        # Start with the initial magic string
        s = [1, 2, 2]
        # i is the index whose value determines how many characters to add
        i = 2 
        
        while len(s) < n:
            # The next number to add alternates between 1 and 2
            # If the last element is 2, next is 1. If last is 1, next is 2.
            # Using (3 - s[-1]) is a neat trick to toggle between 1 and 2
            next_val = 3 - s[-1]
            
            # How many times to add the next_val? Look at s[i]
            num_times = s[i]
            
            for _ in range(num_times):
                if len(s) < n:
                    s.append(next_val)
            
            i += 1
            
        # Return the count of 1s in the first n elements
        return s[:n].count(1)