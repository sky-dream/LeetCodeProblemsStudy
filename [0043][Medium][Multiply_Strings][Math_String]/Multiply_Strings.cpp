// leetcode time     cost : 4 ms
// leetcode memory   cost : 6.7 MB 
// Time  Complexity: O(m*n)
// Space Complexity: O(m+n)
// solution 1, simulate the mannual multiply bit by bit
#include <stdlib.h>
#include <string.h>
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size(), n = num2.size();
        // 结果最多为 m + n 位数
        vector<int> res(m + n, 0);
        // 从个位数开始逐位相乘
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1[i]-'0') * (num2[j]-'0');
                // 乘积在 res 对应的索引位置
                int p1 = i + j, p2 = i + j + 1;
                // 叠加到 res 上
                int sum = mul + res[p2];
                res[p2] = sum % 10;
                res[p1] += sum / 10;
            }
        // 结果前缀可能存的 0（未使用的位）
        int i = 0;
        while (i < res.size() && res[i] == 0)
            i++;
        // 将计算结果转化成字符串
        string str;
        for (; i < res.size(); i++)
            str.push_back('0' + res[i]);
        
        return str.size() == 0 ? "0" : str;
    }
};