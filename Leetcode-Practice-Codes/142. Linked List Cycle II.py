class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: find cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow