#include <string.h>
#include <stdlib.h>
#include <stdio.h>
// #define INT_MAX 2147483647
// #define INT_MIN (-INT_MAX - 1)
// 这里没有简单地将INT_MIN赋值成-2147483647，是因为-2147483648对于编译器而言是个表达式，而2147483648对于32-bit整数是无法表示的，
// 所以经过这个表达式的结果是未定义的。在GCC上直接写-2147483648后，编译器给出了警告，说结果是unsigned。
typedef struct {
    int *data;
    int k;        
} KthLargest;

int compare(const void *arg1, const void *arg2 ) {
    return *(int*)arg2 - *(int*)arg1;
}


KthLargest* kthLargestCreate(int k, int* nums, int numsSize) {
    int i;
    KthLargest* obj = (KthLargest*)malloc(sizeof(KthLargest));
    obj->k = k;
    obj->data = (int*)malloc(sizeof(int)*k);
    qsort(nums, numsSize, sizeof(int), compare);    
    memcpy(obj->data, nums, sizeof(int)*(k>numsSize?numsSize:k));
    for(i=numsSize; i<k; i++){
        obj->data[i] = INT_MIN;
    }
    return obj;
}

int kthLargestAdd(KthLargest* obj, int val) {
    int i;
    for(i=0; i<obj->k; i++){
        if(obj->data[i]<val) {
            if(i+1 != obj->k){
                memmove(obj->data+i+1, obj->data+i, sizeof(int)*(obj->k-i-1));
            }
            obj->data[i] = val;
            break;
        }


    }
    return obj->data[obj->k-1];
}

void kthLargestFree(KthLargest* obj) {
    free(obj->data);
    free(obj);
}

void main(){
    int k = 3;
    int nums[4] = {4,5,8,2};
    int numsSize = sizeof(nums)/sizeof(int);
    KthLargest* obj = kthLargestCreate(k, nums, numsSize);
    int param_1 = kthLargestAdd(obj, 3);
    param_1 = kthLargestAdd(obj, 5);
    param_1 = kthLargestAdd(obj, 10);
    param_1 = kthLargestAdd(obj, 9);
    printf("In c code,last return value is %d",param_1);
    kthLargestFree(obj);
}
/**
 * Your KthLargest struct will be instantiated and called as such:
 * KthLargest* obj = kthLargestCreate(k, nums, numsSize);
 * int param_1 = kthLargestAdd(obj, val);
 
 * kthLargestFree(obj);
*/