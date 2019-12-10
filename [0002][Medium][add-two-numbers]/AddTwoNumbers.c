//Definition for singly-linked list.
/* struct ListNode {
     int val;
    struct ListNode *next;
 }; */

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    int carry_num = 0;
    struct ListNode *currentNode = NULL;
    currentNode = malloc(sizeof(*currentNode));
    struct ListNode *res = currentNode;
    while (l1 != NULL || l2 != NULL || carry_num)
    {
        int sum, value_l1, value_l2;
        value_l1 = (l1 != NULL) ? l1->val : 0;
        value_l2 = (l2 != NULL) ? l2->val : 0;
        sum = value_l1 + value_l2 + carry_num;
        carry_num = sum / 10;
        currentNode->next = malloc(sizeof(*currentNode));
        currentNode->next->val = sum % 10;        
        currentNode->next->next = NULL;
        l1 = l1 != NULL ? l1->next : NULL;
        l2 = l2 != NULL ? l2->next : NULL;
        currentNode = currentNode->next;
    }
    return res->next;
}