import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        # Stores the actual elements to allow O(1) getRandom
        self.lst = []
        # Maps each value to a SET of indices where it appears in self.lst
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        # Check if val is already present before adding
        not_present = val not in self.idx_map or not self.idx_map[val]
        
        self.idx_map[val].add(len(self.lst))
        self.lst.append(val)
        
        return not_present

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        
        # 1. Get an arbitrary index of the value to remove
        remove_idx = self.idx_map[val].pop()
        last_element = self.lst[-1]
        
        # 2. Swap with the last element if it's not the same position
        if remove_idx < len(self.lst) - 1:
            self.lst[remove_idx] = last_element
            # Update the last element's index in the map
            self.idx_map[last_element].remove(len(self.lst) - 1)
            self.idx_map[last_element].add(remove_idx)
            
        # 3. Remove the last element from the list
        self.lst.pop()
        
        return True

    def getRandom(self) -> int:
        # Since duplicates are in the list, random.choice naturally 
        # follows the required probability distribution.
        return random.choice(self.lst)