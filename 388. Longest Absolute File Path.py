class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Stack stores the length of the path up to a certain depth
        # stack[depth] = length of the path at that depth
        stack = {0: 0} # depth 0 has length 0
        max_len = 0
        
        # Split by newlines to process each file/directory individually
        for line in input.split('\n'):
            # The number of '\t' characters tells us the depth
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                # If it's a file, calculate the total length
                # stack[depth] is the parent's path length
                # + length of name + depth (for the number of '/' separators)
                total_len = stack[depth] + len(name)
                max_len = max(max_len, total_len)
            else:
                # If it's a directory, update the stack for the next depth
                # Path length = parent length + name length + 1 (for the '/')
                stack[depth + 1] = stack[depth] + len(name) + 1
                
        return max_len