class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.mapping = {}  # key -> count
        self.nodes = {0: Node(0)}  # count -> Node
        self.head = self.nodes[0]  # dummy head (min)
        self.tail = self.nodes[0]  # dummy tail (max)

    def _add_node_after(self, new_count, prev_node):
        new_node = Node(new_count)
        self.nodes[new_count] = new_node
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        else:
            self.tail = new_node
        prev_node.next = new_node
        return new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        del self.nodes[node.count]

    def inc(self, key: str) -> None:
        cur_count = self.mapping.get(key, 0)
        new_count = cur_count + 1
        self.mapping[key] = new_count
        
        if new_count not in self.nodes:
            self._add_node_after(new_count, self.nodes[cur_count])
        
        self.nodes[new_count].keys.add(key)
        
        if cur_count > 0:
            self.nodes[cur_count].keys.remove(key)
            if not self.nodes[cur_count].keys:
                self._remove_node(self.nodes[cur_count])

    def dec(self, key: str) -> None:
        cur_count = self.mapping[key]
        new_count = cur_count - 1
        
        if new_count == 0:
            del self.mapping[key]
        else:
            self.mapping[key] = new_count
            if new_count not in self.nodes:
                # To maintain order, insert new_count node BEFORE cur_count node
                # Since we know cur_count > new_count, we insert after cur_count.prev
                self._add_node_after(new_count, self.nodes[cur_count].prev)
            self.nodes[new_count].keys.add(key)
            
        self.nodes[cur_count].keys.remove(key)
        if not self.nodes[cur_count].keys:
            self._remove_node(self.nodes[cur_count])

    def getMaxKey(self) -> str:
        if self.tail == self.head: return ""
        return next(iter(self.tail.keys))

    def getMinKey(self) -> str:
        if self.head.next is None: return ""
        return next(iter(self.head.next.keys))