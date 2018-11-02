import java.math.*;
public class Leetcode382{

 //Definition for singly-linked list.
 	public class ListNode {
    	int val;
    	ListNode next;
    	ListNode(int x) { val = x; }
  	}
 

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Leetcode382(ListNode head) {
        ListNode Head = head;
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        int size = getSize();
        int random = (int )(Math. random() * size);
        int i = 0;
        ListNode pointnode = Head;
        while (i != random){
        	i = i + 1;
        	pointnode = pointnode.next;
        }
        int getvalue = pointnode.val;

        return getvalue;

    }
    /*Return the size of the ListNode head*/
    public int getSize() {
        int size = 1;
        ListNode pointnode = Head;
        while (pointnode.next != null) {
        	size = size + 1;
        	pointnode = pointnode.next;
        }
        return size;
    }


/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */

public static void main(String[] args) {
    ListNode lst = new ListNode(11);
    lst.next = new ListNode(12);
    lst.next.next = new ListNode(13);
    lst.next.next.next = null;
    Leetcode382 test = new Leetcode382(lst);
  	int param_1 = test.getRandom();
    System.out.println(param_1);
    }

}