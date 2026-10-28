class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = [0] * 26
        s_count = [0] * 26
        res = []

        # Initialize the frequency map for p and the first window of s
        for i in range(np):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        # Check the first window
        if p_count == s_count:
            res.append(0)

        # Slide the window across s
        for i in range(np, ns):
            # Add the new character (right side)
            s_count[ord(s[i]) - ord('a')] += 1
            # Remove the old character (left side)
            s_count[ord(s[i - np]) - ord('a')] -= 1
            
            # Compare maps
            if p_count == s_count:
                res.append(i - np + 1)

        return res