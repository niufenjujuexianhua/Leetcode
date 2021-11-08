/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        Node p = head; 
        // Traverse the list
        while (p != null) {
            if (p.child != null) {
                Node right = p.next; 
                
                //Process child
                p.next = flatten(p.child);
                p.next.prev = p;
                p.child = null; 
                         
                while (p.next != null)
                    p = p.next;
                
                //Reconnect next 
                if (right != null) { 
                    p.next = right;
                    p.next.prev = p; 
                }
            }
            p = p.next;
        }
        return head; 
    }
}