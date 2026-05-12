class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        
        while i < len(words):
            # Step 1: pack words
            line_len = len(words[i])
            j = i + 1
            
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            spaces = maxWidth - sum(len(w) for w in line_words)
            slots = len(line_words) - 1
            
            # Step 2: build line
            # Case 1: last line OR single word
            if j == len(words) or slots == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                space_per_slot = spaces // slots
                extra = spaces % slots
                
                line = ""
                for k in range(slots):
                    line += line_words[k]
                    line += " " * (space_per_slot + (1 if k < extra else 0))
                line += line_words[-1]
            
            res.append(line)
            i = j
        
        return res