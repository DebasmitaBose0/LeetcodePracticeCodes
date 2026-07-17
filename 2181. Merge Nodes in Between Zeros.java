
class Solution {
    public ListNode mergeNodes(ListNode head) {
        
        ListNode modify = head.next;
        
        ListNode current = head.next;
        
        while (current != null) {
            int runningSum = 0;
            
            while (current != null && current.val != 0) {
                runningSum += current.val;
                current = current.next;
            }
            
            
            modify.val = runningSum;
            
            current = current.next;
           
            modify.next = current;
            modify = modify.next;
        }
        
        return head.next;
    }
}