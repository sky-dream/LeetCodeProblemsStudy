/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    int i, j;
    int head, tail;

    int *ret;
    int *queue;

    if (nums == NULL || numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    *returnSize = (numsSize - k + 1);
    ret = malloc(sizeof(int) * (*returnSize));

    /*An array to store all numbers might potentially be the maximum of the K size window, it works similarly with a queue */
    queue = malloc(sizeof(int) * numsSize);
    memset(queue, 0, sizeof(int) * numsSize);
    head = 0;
    tail = -1;
    j = 0;

    for (i = 0; i < numsSize; i ++) {
        /* Remove the items in the queue but smaller  than current item. This is O(n) as each item will only go into queue once 
        * and we will totally compare n times in maximum  
        */
        while (tail >= head && nums[i] > nums[queue[tail]]) {
            tail --;
        }
        queue[ ++ tail] = i;
        if (i - j + 1 == k) {
            ret[j ++] = nums[queue[head]];
        }
        while (head <= tail && i - queue[head] + 1 >= k) {
            head ++;
        }
    }

    free(queue);

    return ret;
}