class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Number of bytes remaining in the current UTF-8 character
        n_bytes = 0
        
        # Mask to check the leading bits
        mask1 = 1 << 7 # 10000000
        mask2 = 1 << 6 # 01000000
        
        for num in data:
            # We only care about the 8 least significant bits
            byte = num & 0xFF
            
            if n_bytes == 0:
                # Determine how many bytes the current character has
                mask = 1 << 7
                while mask & byte:
                    n_bytes += 1
                    mask >>= 1
                
                # 1-byte character: starts with 0 (n_bytes is 0)
                if n_bytes == 0:
                    continue
                
                # UTF-8 characters can only be 1 to 4 bytes long
                # Also, a multi-byte character cannot start with '10' (n_bytes == 1)
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                # Following bytes must start with '10'
                if not (byte & mask1 and not (byte & mask2)):
                    return False
            
            # We processed one byte of the current multi-byte character
            n_bytes -= 1
            
        # If n_bytes is not 0, it means we were expecting more bytes
        return n_bytes == 0