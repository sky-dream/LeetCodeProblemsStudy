// solution 4, multiset and 1 single pointer, more diffcult to understand..
// leetcode time     cost : 244 ms
// leetcode memory   cost : 44.5 MB
// Time  Complexity: O(NlogN)
// Space Complexity: O(N)
#include <set>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

class MedianFinder {
    multiset<int> data;
    multiset<int>::iterator mid;

public:
    MedianFinder()
        : mid(data.end())
    {
    }

    void addNum(int num)
    {
        const int n = data.size();
        data.insert(num);

        if (!n)                                 // first element inserted
            mid = data.begin();
        else if (num < *mid)                    // median is decreased
            mid = (n & 1 ? mid : prev(mid));
        else                                    // median is increased
            mid = (n & 1 ? next(mid) : mid);
    }

    double findMedian()
    {
        const int n = data.size();
        return (*mid + *next(mid, n % 2 - 1)) * 0.5;
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