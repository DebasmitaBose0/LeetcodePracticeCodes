class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def is_ipv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                # Check if part is a digit and not empty
                if not part.isdigit():
                    return False
                # Check for leading zeros: '0' is fine, but '01' is not
                if len(part) > 1 and part[0] == '0':
                    return False
                # Check value range
                if not (0 <= int(part) <= 255):
                    return False
            return True

        def is_ipv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hex_digits = "0123456789abcdefABCDEF"
            for part in parts:
                # Length must be between 1 and 4
                if not (1 <= len(part) <= 4):
                    return False
                # Must be valid hex characters
                if not all(c in hex_digits for c in part):
                    return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"