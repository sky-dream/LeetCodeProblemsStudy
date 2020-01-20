#include <string.h>
#include <stdlib.h>
#include<iostream>
#include <queue>
using namespace std;
class KthLargest {
	priority_queue<int, vector<int>, greater<int>> *q;
	int size;
public: 
    KthLargest(int k, vector<int>& nums) {
		size = k;
		q = new priority_queue<int, vector<int>, greater<int>>(size,INT_MIN);
		for (auto c : nums) {
			add(c);
		}
	}

	int add(int val) {
		if (val < (*q).top())
			return (*q).top();
		else {
			(*q).pop();
			(*q).push(val);
		}
		return (*q).top();
	}
};

int main(){
    int k = 3;
    vector<int> nums= {4,5,8,2};
    int numsSize = sizeof(nums)/sizeof(int);
    KthLargest *obj = new KthLargest(k, nums);
    int param_1 = obj->add(3);
    param_1 = obj->add(5);
    param_1 = obj->add(10);
    param_1 = obj->add(9);
    cout << "In cpp code,last return value is " << param_1 << '\n';
	cout << endl;
    delete(obj);
	return 0;
}
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
