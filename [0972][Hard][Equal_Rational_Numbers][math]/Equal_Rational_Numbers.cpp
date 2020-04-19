// leetcode time     cost : 0 ms
// leetcode memory   cost : 6.1 MB 
// Time  Complexity: O(1)
// Space  Complexity: O(1)
// compare the first 8 digits after the spot
#include <string>
#include <stdlib.h>
using namespace std;
class Solution {
public:
    bool isRationalEqual(string S, string T) {
        return conv(S) == conv(T);
    }
    string conv(string& s) {
        // 去除前导零
        if(s[0] == '0' && s[1] >= '0' && s[1] <= '9')
            s.erase(s.begin());
        
        // 找到小数点、左括号、右括号
        size_t point = s.find("."), left = s.find("("), right = s.find(")");
        if(point == string::npos) { // 如果没有小数点就添加一个
            s += '.';
            point = s.size() - 1;
        }

        // 将循环小数展开成小数点后 8 位小数
        string rep = "0" ;
        if(left != string::npos) {
            rep = s.substr(left + 1, right - left - 1);
            s = s.substr(0, left);
        }
        while(s.size() - point - 1 < 8)
            s += rep;
        s = s.substr(0,9 + point);

        // 如果循环部分是 99.. 则进位
        for(int i = 0; i < rep.size(); ++i)
            if(rep[i] != '9')
                return s;
        int p = s.size() - 1;
        for(; s[p] == '9' || s[p] == '.'; --p) {
            if(s[p] != '.')
                s[p] = '0';
            if(p == 0)
                return '1' + s;
        }
        s[p] += 1;
        return s;
    }  
};