// solution 3, 2 priority queue
// leetcode time     cost : 328 ms
// leetcode memory   cost : 41.7 MB
// Time  Complexity: O(logN)
// Space Complexity: O(N)
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

class MedianFinder {
    priority_queue<int> max_heap;                              // max heap
    priority_queue<int, vector<int>, greater<int>> min_heap;   // min heap

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        max_heap.push(num);                      // Add to max heap

        min_heap.push(max_heap.top());             // balancing step
        max_heap.pop();

        if (max_heap.size() < min_heap.size()) {      // maintain size property
            max_heap.push(min_heap.top());
            min_heap.pop();
        }
    }

    // Returns the median of current data stream
    double findMedian()
    {
        return max_heap.size() > min_heap.size() ? (double) max_heap.top() : (max_heap.top() + min_heap.top()) * 0.5;
    }
};

int main(){
    MedianFinder* obj = new MedianFinder();
    obj->addNum(1);
    obj->addNum(2);
    obj->addNum(3);
    double param_2 = obj->findMedian();
    cout<<param_2;
    return 0;
}