import random

class RandomizedSet:

    def __init__(self):
        self.data_map = {}  # val -> index
        self.data_list = [] # elements

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        
        # Element to remove and its index
        idx_to_remove = self.data_map[val]
        last_element = self.data_list[-1]
        
        # Move last element to the spot of the element we're deleting
        self.data_list[idx_to_remove] = last_element
        self.data_map[last_element] = idx_to_remove
        
        # Remove the last element from both structures
        self.data_list.pop()
        del self.data_map[val]
        return True

    def getRandom(self) -> int:
        # Since all elements are in a list, we can pick a random index
        return random.choice(self.data_list)