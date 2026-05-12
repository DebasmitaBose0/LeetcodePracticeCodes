from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None) # Dummy head
        self.tail = Node(None, None) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def pop_tail(self):
        if self._size == 0: return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {} # key -> node
        self.freq_map = defaultdict(DoublyLinkedList) # freq -> DoublyLinkedList

    def _update_freq(self, node):
        # Remove from old frequency list
        freq = node.freq
        self.freq_map[freq].remove(node)
        
        # If the old freq list is empty and was the min_freq, increment min_freq
        if self.min_freq == freq and self.freq_map[freq]._size == 0:
            self.min_freq += 1
            
        # Increment node freq and add to new list
        node.freq += 1
        self.freq_map[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return

        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                # Evict LFU (LRU if tie)
                lfu_list = self.freq_map[self.min_freq]
                evicted_node = lfu_list.pop_tail()
                del self.key_map[evicted_node.key]
                self.size -= 1
            
            # Add new node
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].add_front(new_node)
            self.min_freq = 1
            self.size += 1