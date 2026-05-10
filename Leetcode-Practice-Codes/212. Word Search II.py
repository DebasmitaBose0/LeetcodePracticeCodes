class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word when ending


class Solution:
    def findWords(self, board, words):
        # build trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            ch = board[r][c]
            
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates
            
            board[r][c] = "#"  # mark visited
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            
            board[r][c] = ch  # restore
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result