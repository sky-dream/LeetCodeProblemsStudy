/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
int *maxSlidingWindow(int *nums, int numsSize, int k, int *returnSize)
{
    int i, j;
    int head, tail;

    int *ret;
    int *queue;

    if (nums == NULL || numsSize == 0)
    {
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

    for (i = 0; i < numsSize; i++)
    {
        /* Remove the items in the queue but smaller  than current item. This is O(n) as each item will only go into queue once 
        * and we will totally compare n times in maximum  
        */
        while (tail >= head && nums[i] > nums[queue[tail]])
        {
            tail--;
        }
        queue[++tail] = i;
        if (i - j + 1 == k)
        {
            ret[j++] = nums[queue[head]];
        }
        while (head <= tail && i - queue[head] + 1 >= k)
        {
            head++;
        }
    }

    free(queue);

    return ret;
}

void main()
{
    int k = 0;
    int i;
    int returnSize = 0;
    int nums[9] = {9, 3, -1, -3, 5, 3, 6, 7, -3}; //#expect is [9,3,5,5,6,7,7]
    int numsSize = sizeof(nums) / sizeof(int);
    int *result = maxSlidingWindow(nums, 9, 3, &returnSize);
    printf("In c code , maxSlidingWindow array result  is : [");
    for (i = 0; i < returnSize; i++)
    {
        printf(" %d ,", result[i]);
    }
    printf(" ] \n");
}