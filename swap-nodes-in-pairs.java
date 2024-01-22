//Link : https://leetcode.com/problems/swap-nodes-in-pairs/



import java.util.LinkedList;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next==null)
        return head;
        ListNode dummy = new ListNode();
        ListNode prev= dummy;
        ListNode current= head;
        while (current!= null && current.next!=null){
            ListNode nextpair = current.next.next;
            ListNode second= current.next;
            second.next=current;
            current.next=nextpair;
            prev.next=second;
            prev=current;
            current=nextpair;
        }
        return dummy.next;
    }
}
