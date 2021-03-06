// -*- coding: utf-8 -*- 
// leetcode time     cost : 0 ms
// leetcode memory   cost : 5.9 MB
// Time  Complexity: O(logX)
// Space Complexity: O(1)
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
/*
使用32位存储。
INT_MAX的值为+2147483647。
INT_MIN的值为-2147483648。
*/