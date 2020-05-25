
struct ListNode {
    int val;
    struct ListNode next;
};


// leetcode time     cost : 68 ms
// leetcode memory   cost : 13.5 MB
// Time  Complexity: O(m+n)
// Space Complexity: O(1)
 // solution 3, 2 pointers
struct ListNode getIntersectionNode(struct ListNode headA, struct ListNode headB) {
    if(!headA || !headB) return NULL;
    struct ListNode p, q, pp, qq;
    p = headA; q = headB;
    while(p != q)
    {
        pp = p; qq = q;
        p = (!p -> next && qq -> next) ? headB : p -> next;
        q = (!q -> next && pp -> next) ? headA : q -> next;
    }
    return p;
}