class Solution:
    def modifiedList(self, nums, head):
        remove_set = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next:
            if curr.next.val in remove_set:
                curr.next = curr.next.next  # remove node
            else:
                curr = curr.next
        
        return dummy.next