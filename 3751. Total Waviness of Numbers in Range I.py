class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            # Numbers with fewer than 3 digits have a waviness of 0
            if num < 100:
                continue
                
            s = str(num)
            # Check every digit except the first and last
            for i in range(1, len(s) - 1):
                prev_digit = s[i - 1]
                curr_digit = s[i]
                next_digit = s[i + 1]
                
                # Peak condition: strictly greater than both neighbors
                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1
                # Valley condition: strictly less than both neighbors
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
                    
        return total_waviness