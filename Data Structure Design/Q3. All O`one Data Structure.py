class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.root = Node(0)  # Sentinel head
        self.root.next = self.root
        self.root.prev = self.root
        self.mapping = {}  # key -> Node

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        return new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.mapping:
            if self.root.next == self.root or self.root.next.count != 1:
                self._add_node_after(Node(1), self.root)
            self.root.next.keys.add(key)
            self.mapping[key] = self.root.next
        else:
            cur_node = self.mapping[key]
            next_node = cur_node.next
            if next_node == self.root or next_node.count != cur_node.count + 1:
                next_node = self._add_node_after(Node(cur_node.count + 1), cur_node)
            next_node.keys.add(key)
            self.mapping[key] = next_node
            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove_node(cur_node)

    def dec(self, key: str) -> None:
        cur_node = self.mapping[key]
        if cur_node.count == 1:
            del self.mapping[key]
        else:
            prev_node = cur_node.prev
            if prev_node == self.root or prev_node.count != cur_node.count - 1:
                prev_node = self._add_node_after(Node(cur_node.count - 1), cur_node.prev)
            prev_node.keys.add(key)
            self.mapping[key] = prev_node
        
        cur_node.keys.remove(key)
        if not cur_node.keys:
            self._remove_node(cur_node)

    def getMaxKey(self) -> str:
        if self.root.prev == self.root:
            return ""
        return next(iter(self.root.prev.keys))

    def getMinKey(self) -> str:
        if self.root.next == self.root:
            return ""
        return next(iter(self.root.next.keys))