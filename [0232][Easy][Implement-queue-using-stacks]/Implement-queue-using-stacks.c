#define MAX_SIZE 128 //假定最大的栈空间为128
//先定义一个栈结构
typedef struct
{
    int arr[MAX_SIZE];
    int top;
    int front; //用来保存s1的队头元素
} MyStack;
//队列由两个栈组成
typedef struct
{
    MyStack S1;
    MyStack S2;
} MyQueue;

/** Initialize your data structure here. */
//创建的时候初始化数据
MyQueue *myQueueCreate()
{
    MyQueue *Q = (MyQueue *)malloc(sizeof(MyQueue));
    if (!Q)
        return NULL;
    Q->S1.top = -1;
    Q->S1.front = -1;
    Q->S2.top = -1;
    Q->S2.front = -1;
    return Q;
}
//入栈的时候，用s1入栈，保存一个队头元素front
/** Push element x to the back of queue. */
void myQueuePush(MyQueue *obj, int x)
{
    if (!obj)
        return;
    if (obj->S1.top != MAX_SIZE)
    {
        obj->S1.arr[++obj->S1.top] = x;
        if (obj->S1.top == 0)
            obj->S1.front = x;
    }
}
//出栈的时候，把s1的元素都push进s2，然后通过s2出栈
/** Removes the element from in front of queue and returns that element. */
int myQueuePop(MyQueue *obj)
{
    if (obj->S2.top == -1)
    {
        while (obj->S1.top != -1)
        {
            obj->S2.arr[++obj->S2.top] = obj->S1.arr[obj->S1.top--];
        }
    }
    return obj->S2.arr[obj->S2.top--];
}

/** Get the front element. */
//如果s1不为空，就返回s1的front，否则返回s2的栈顶元素
int myQueuePeek(MyQueue *obj)
{
    if (obj->S2.top != -1)
    {
        return obj->S2.arr[obj->S2.top];
    }
    return obj->S1.front;
}

/** Returns whether the queue is empty. */
bool myQueueEmpty(MyQueue *obj)
{
    return obj->S2.top == -1 && obj->S1.top == -1;
}

void myQueueFree(MyQueue *obj)
{
    free(obj);
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);
 
 * int param_2 = myQueuePop(obj);
 
 * int param_3 = myQueuePeek(obj);
 
 * bool param_4 = myQueueEmpty(obj);
 
 * myQueueFree(obj);
*/