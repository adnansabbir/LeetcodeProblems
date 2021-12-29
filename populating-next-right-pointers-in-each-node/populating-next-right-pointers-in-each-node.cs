/*
// Definition for a Node.
public class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}
*/

public class Solution {
    public Node Connect(Node root, Node next=null) {
        if(root==null) return root;
        
        root.next = next;
        
        Node nextForLeft = root.right;
        Node nextForRight = next!=null? next.left : null;
        
        Connect(root.left, nextForLeft);
        Connect(root.right, nextForRight);
        
        return root;
    }
}