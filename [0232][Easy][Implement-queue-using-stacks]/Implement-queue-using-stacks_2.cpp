class MyQueue
{
public:
    /** Initialize your data structure here. */
    MyQueue()
    {
        stack_A = new std::stack<int>;
        stack_B = new std::stack<int>;
    }

    /** Push element x to the back of queue. */
    void push(int x)
    {
        stack_A->push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop()
    {
        if (stack_A->empty())
        {
            return false;
        }
        else
        {
            while (!stack_B->empty())
            {
                stack_B->pop();
            }
            int x = 0;
            while (!stack_A->empty())
            {
                x = stack_A->top();
                stack_B->push(x);
                stack_A->pop();
            }
            int result = stack_B->top();
            stack_B->pop();
            int y = 0;
            while (!stack_B->empty())
            {
                y = stack_B->top();
                stack_A->push(y);
                stack_B->pop();
            }
            return result;
        }
    }

    /** Get the front element. */
    int peek()
    {
        int result = 0;
        if (stack_A->empty())
        {
            return false;
        }
        else
        {
            int a = 0;
            while (!stack_B->empty())
            {
                stack_B->pop();
            }
            while (!stack_A->empty())
            {
                a = stack_A->top();
                stack_B->push(a);
                stack_A->pop();
            }
            result = stack_B->top();
            while (!stack_B->empty())
            {
                a = stack_B->top();
                stack_A->push(a);
                stack_B->pop();
            }
        }
        return result;
    }

    /** Returns whether the queue is empty. */
    bool empty()
    {
        return stack_A->empty();
    }

private:
    std::stack<int> *stack_A;
    std::stack<int> *stack_B;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */