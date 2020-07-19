// solution 2, 2 pointers
// Time  Complexity: O(N)
// Space Complexity: O(1)
import java.util.HashSet;
import java.util.HashSet;
import java.util.ListNode;
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}
