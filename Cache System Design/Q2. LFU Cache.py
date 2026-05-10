class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0) # Dummy head
        self.tail = Node(0, 0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0: return None
        node = self.tail.prev
        self.remove_node(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.cache = {} # key -> Node
        self.freq_map = {} # freq -> DoublyLinkedList

    def _update_freq(self, node):
        """Moves a node from its current frequency list to freq + 1."""
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        # If the current min_freq list is empty, increment min_freq
        if self.freq_map[freq].size == 0 and freq == self.min_freq:
            self.min_freq += 1
            
        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                # Evict the LRU node from the min_freq list
                lfu_list = self.freq_map[self.min_freq]
                evicted_node = lfu_list.remove_tail()
                if evicted_node:
                    del self.cache[evicted_node.key]
                    self.size -= 1
                
            # Create the new node and add it to the freq 1 list
            new_node = Node(key, value)
            self.cache[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1
            self.size += 1