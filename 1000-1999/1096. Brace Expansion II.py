class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Find the split index for commas, ignoring commas inside curly braces
        def find_top_level_commas(s):
            commas = []
            level = 0
            for idx, char in enumerate(s):
                if char == '{':
                    level += 1
                elif char == '}':
                    level -= 1
                elif char == ',' and level == 0:
                    commas.append(idx)
            return commas

        # Parse expressions by breaking down products and unions
        def parse(s):
            if not s:
                return set()
            
            # 1. Handle commas (Unions) at the top level
            commas = find_top_level_commas(s)
            if commas:
                result = set()
                prev = 0
                for c in commas:
                    result.update(parse(s[prev:c]))
                    prev = c + 1
                result.update(parse(s[prev:]))
                return result
            
            # 2. Handle braces {...}
            if s[0] == '{' and s[-1] == '}':
                # Check if these outer braces enclose the entire expression without breaking early
                level = 0
                matched = True
                for i in range(len(s) - 1):
                    if s[i] == '{': level += 1
                    elif s[i] == '}': level -= 1
                    if level == 0:
                        matched = False
                        break
                if matched:
                    return parse(s[1:-1])

            # 3. Handle concatenations (split into individual product chunks)
            # Find chunks: either a single letter, or a {...} block
            i = 0
            res = {""}  # Start with an empty string for cartesian product accumulation
            while i < len(s):
                if s[i] == '{':
                    # Find matching closing brace
                    start = i
                    level = 0
                    while i < len(s):
                        if s[i] == '{': level += 1
                        elif s[i] == '}': level -= 1
                        i += 1
                        if level == 0: break
                    block = s[start:i]
                    sub_set = parse(block)
                    res = {a + b for a in res for b in sub_set}
                else:
                    # Single letter term
                    start = i
                    while i < len(s) and s[i].isalpha():
                        i += 1
                    term = s[start:i]
                    res = {a + term for a in res}
            
            return res

        return sorted(list(parse(expression)))