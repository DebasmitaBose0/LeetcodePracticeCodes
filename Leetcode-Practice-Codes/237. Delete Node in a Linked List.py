class Solution:
    def deleteNode(self, node):
        node.val = node.next.val      # Copy next node's value
        node.next = node.next.next    # Skip next node