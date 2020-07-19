// solution 1, set
// Time  Complexity: O(N)
// Space Complexity: O(N)
import java.util.HashSet;
import java.util.HashSet;
import java.util.ListNode;
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodesSeen = new HashSet<>();
        while (head != null) {
            if (nodesSeen.contains(head)) {
                return true;
            } else {
                nodesSeen.add(head);
            }
            head = head.next;
        }
        return false;
    }
}
