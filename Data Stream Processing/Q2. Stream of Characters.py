class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.history = []
        # We only care about suffixes up to the length of the longest word
        self.max_len = 0
        
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.root
            # Insert word into Trie in reverse
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        
        # Keep history within reasonable bounds
        if len(self.history) > self.max_len:
            self.history.pop(0)
            
        node = self.root
        # Check suffixes by traversing history backwards
        for i in range(len(self.history) - 1, -1, -1):
            char = self.history[i]
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_word:
                return True
        return False