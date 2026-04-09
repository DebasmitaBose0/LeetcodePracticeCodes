import random

class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        # Map value to its future index (end of the list)
        self.indices[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        # Get index of the element to remove and the last element in the list
        idx_to_remove = self.indices[val]
        last_element = self.list[-1]
        
        # Move the last element to the spot of the element we're removing
        self.list[idx_to_remove] = last_element
        self.indices[last_element] = idx_to_remove
        
        # Remove the last element from both structures
        self.list.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)