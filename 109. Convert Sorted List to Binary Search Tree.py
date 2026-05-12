class Solution:
    def sortedListToBST(self, head):
        def findMid(head):
            prev = None
            slow = fast = head
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev:
                prev.next = None
            
            return slow
        
        if not head:
            return None
        
        mid = findMid(head)
        root = TreeNode(mid.val)
        
        if head == mid:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root