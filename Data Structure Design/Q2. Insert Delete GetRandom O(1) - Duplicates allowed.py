import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.data_map = defaultdict(set)
        self.data_list = []

    def insert(self, val: int) -> bool:
        # A value is "present" only if its index set is not empty
        present = len(self.data_map[val]) > 0
        
        self.data_map[val].add(len(self.data_list))
        self.data_list.append(val)
        
        return not present

    def remove(self, val: int) -> bool:
        if not self.data_map[val]:
            return False
        
        # 1. Get an arbitrary index of the value to remove
        remove_idx = self.data_map[val].pop()
        last_element = self.data_list[-1]
        last_idx = len(self.data_list) - 1
        
        # 2. Swap logic
        self.data_list[remove_idx] = last_element
        
        # 3. Update the map for the moved last_element
        # IMPORTANT: Add the new index BEFORE discarding the old one
        # to handle the case where remove_idx == last_idx
        self.data_map[last_element].add(remove_idx)
        self.data_map[last_element].discard(last_idx)
        
        # 4. Cleanup the list
        self.data_list.pop()
            
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_list)