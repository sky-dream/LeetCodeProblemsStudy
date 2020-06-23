// solution 1, simple sorting
// leetcode time     cost : -- ms
// leetcode memory   cost : -- MB
// Time  Complexity: O(NlogN)
// Space Complexity: O(N)
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

class MedianFinder {
    vector<double> store;

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        store.push_back(num);
    }

    // Returns the median of current data stream
    double findMedian()
    {
        sort(store.begin(), store.end());

        int n = store.size();
        return (n & 1 ? store[n / 2] : (store[n / 2 - 1] + store[n / 2]) * 0.5);
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