class MyQueue
{
public:
    /** Initialize your data structure here. */
    stack<int> a;
    stack<int> b;
    MyQueue()
    {
    }

    /** Push element x to the back of queue. */
    void push(int x)
    {
        a.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop()
    {
        int len;
        len = a.size();
        for (int i = 0; i < len; ++i)
        {
            b.push(a.top());
            a.pop();
        }
        int cur;
        cur = b.top();
        b.pop();
        for (int j = 0; j < len - 1; ++j)
        {
            a.push(b.top());
            b.pop();
        }
        return cur;
    }

    /** Get the front element. */
    int peek()
    {
        int len;
        len = a.size();
        for (int i = 0; i < len; ++i)
        {
            b.push(a.top());
            a.pop();
        }
        int cur;
        cur = b.top();
        for (int j = 0; j < len; ++j)
        {
            a.push(b.top());
            b.pop();
        }
        return cur;
    }

    /** Returns whether the queue is empty. */
    bool empty()
    {
        return a.empty() && b.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */