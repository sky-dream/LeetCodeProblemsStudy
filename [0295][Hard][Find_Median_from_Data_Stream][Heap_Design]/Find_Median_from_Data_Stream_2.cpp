// solution 2, insert sorting
// leetcode time     cost : 452 ms
// leetcode memory   cost : 41.9 MB
// Time  Complexity: O(N+logN)=O(N)
// Space Complexity: O(N)
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

class MedianFinder {
    vector<int> store; // resize-able container

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        if (store.empty())
            store.push_back(num);
        else
            // binary search and insertion combined
            store.insert(lower_bound(store.begin(), store.end(), num), num);     
    }

    // Returns the median of current data stream
    double findMedian()
    {
        int n = store.size();
        return n & 1 ? store[n / 2] : (store[n / 2 - 1] + store[n / 2]) * 0.5;
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