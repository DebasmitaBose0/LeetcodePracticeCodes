class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the best matching word passing through this node
        self.best_index = -1 

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        
        # 1. Find the global default best index (smallest length, earliest occurrence)
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
                
        # Initialize the root node with the global best index
        root.best_index = global_best_idx
        
        # 2. Build the Trie with reversed words
        for idx, word in enumerate(wordsContainer):
            curr = root
            # Traverse backwards to handle suffix as prefix
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update the best_index at the current node if applicable
                if curr.best_index == -1:
                    curr.best_index = idx
                else:
                    curr_best_len = len(wordsContainer[curr.best_index])
                    if len(word) < curr_best_len:
                        curr.best_index = idx
                    # Tie-breaker: earlier index wins (idx > curr.best_index always here, 
                    # so we don't need to update if lengths are equal)

        # 3. Process the queries
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            # The node we ended up at holds the index to the best string sharing this prefix
            ans.append(curr.best_index)
            
        return ans