class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(num: int) -> int:
            if num < 100:
                return 0
            
            s = str(num)
            n = len(s)
            
            # Memoization table: (index, last_digit, second_last_digit, is_tight, is_started)
            # Returns a tuple: (count_of_valid_numbers, total_waviness_sum)
            memo = {}
            
            def dfs(idx, last, sec_last, is_tight, is_started):
                # Base case: completed building the number
                if idx == n:
                    return (1, 0) if is_started else (0, 0)
                
                state = (idx, last, sec_last, is_tight, is_started)
                if state in memo:
                    return memo[state]
                
                limit = int(s[idx]) if is_tight else 9
                total_count = 0
                total_wave = 0
                
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    
                    if not is_started:
                        if d == 0:
                            # Leading zeros: skip treating this as a valid digit
                            cnt, wave = dfs(idx + 1, -1, -1, next_tight, False)
                            total_count += cnt
                            total_wave += wave
                        else:
                            # First non-zero digit found
                            cnt, wave = dfs(idx + 1, d, -1, next_tight, True)
                            total_count += cnt
                            total_wave += wave
                    else:
                        # We have at least one digit already
                        new_wave_point = 0
                        if sec_last != -1:
                            # Check if the 'last' digit is a peak or a valley
                            # because now we have its left neighbor (sec_last) and right neighbor (d)
                            if last > sec_last and last > d:
                                new_wave_point = 1  # Peak
                            elif last < sec_last and last < d:
                                new_wave_point = 1  # Valley
                        
                        cnt, wave = dfs(idx + 1, d, last, next_tight, True)
                        
                        total_count += cnt
                        # Total waviness contributed by downstream path + 
                        # the waviness created at the 'last' position across all valid branches
                        total_wave += wave + (cnt * new_wave_point)
                
                memo[state] = (total_count, total_wave)
                return memo[state]
            
            return dfs(0, -1, -1, True, False)[1]
        
        return solve(num2) - solve(num1 - 1)