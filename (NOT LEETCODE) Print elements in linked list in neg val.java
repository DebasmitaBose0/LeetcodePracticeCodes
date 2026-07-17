class Solution{

public void printAllAsNegative(Node head) {
    Node current = head;
    while (current != null) {
        // Force the value to be negative
        int negativeVal = -Math.abs(current.value);
        System.out.print(negativeVal + " ");
        current = current.next;
    }
}
}
