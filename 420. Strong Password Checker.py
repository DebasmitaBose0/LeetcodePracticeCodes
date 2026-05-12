class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        missing_types = (1 - has_lower) + (1 - has_upper) + (1 - has_digit)
        
        # Track repeating groups lengths (>= 3)
        repeats = []
        i = 0
        while i < n:
            length = 1
            while i + 1 < n and password[i] == password[i+1]:
                length += 1
                i += 1
            if length >= 3:
                repeats.append(length)
            i += 1

        if n < 6:
            return max(6 - n, missing_types)
        
        elif n <= 20:
            replacements = sum(length // 3 for length in repeats)
            return max(replacements, missing_types)
        
        else:
            deletions = n - 20
            # Step 1: Use deletions to reduce groups where length % 3 == 0 (costs 1 del)
            for i in range(len(repeats)):
                if deletions <= 0: break
                if repeats[i] % 3 == 0:
                    repeats[i] -= 1
                    deletions -= 1
            
            # Step 2: Use deletions to reduce groups where length % 3 == 1 (costs 2 del)
            for i in range(len(repeats)):
                if deletions <= 0: break
                if repeats[i] % 3 == 1:
                    can_delete = min(deletions, 2)
                    repeats[i] -= can_delete
                    deletions -= can_delete
            
            # Step 3: Use remaining deletions on any group (costs 3 del)
            for i in range(len(repeats)):
                if deletions <= 0: break
                if repeats[i] >= 3:
                    can_delete = min(deletions, repeats[i] - 2)
                    repeats[i] -= can_delete
                    deletions -= can_delete
            
            replacements = sum(length // 3 for length in repeats)
            return (n - 20) + max(replacements, missing_types)