class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {c: i for i, c in enumerate(s)}
        last = {c: i for i, n_idx in enumerate(s) for c in [n_idx]}  # or standard reverse loop
        
        # Better way to get first and last occurrences
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        intervals = []
        for c in first:
            # Try to find a valid substring starting at first[c]
            start = first[c]
            end = last[c]
            valid = True
            
            i = start
            while i <= end:
                # If a character appears earlier than our start, this interval is invalid
                if first[s[i]] < start:
                    valid = False
                    break
                # Expand the end boundary if necessary
                end = max(end, last[s[i]])
                i += 1
                
            if valid:
                intervals.append([start, end])
                
        # Greedily select non-overlapping intervals (sorted by end time, then start time)
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end+1])
                prev_end = end
                
        Id = res
        return res