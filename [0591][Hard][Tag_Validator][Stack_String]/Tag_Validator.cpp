// leetcode time     cost : 4 ms
// leetcode memory   cost : 8.2 MB
// Time  Complexity: O(n)
// Space Complexity: O(n)
// solution 3, string.
/*
tag :
    <tagname> + content + </tagname>
tagname : 
    [A-Z]{1, 9}                 # 1 ~ 9 uppercase chars
content : 
    (tag|cdata|text)*           # 0 or more of : tag, cdata, text
cdata : 
    "<![CDATA[" + .* + "]]>"
text :
    [^<]+                       # non '<' chars
*/
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;
class Solution {
public:
    bool isValid(string code) {
        int i = 0;
        return validTag(code, i) && i == code.size();
    }

private:
    bool validTag(string s, int& i) {
        int j = i;
        string tag = parseTagName(s, j);
        if (tag.empty()) return false;
        if (!validContent(s, j)) return false;
        int k = j + tag.size() + 2; // expecting j = pos of "</" , k = pos of '>'
        if (k >= s.size() || s.substr(j, k + 1 - j) != "</" + tag + ">") return false;
        i = k + 1;
        return true;
    }

    string parseTagName(string s, int& i) {
        if (s[i] != '<') return "";
        int j = s.find('>', i);
        if (j == string::npos || j - 1 - i < 1 || 9 < j - 1 - i) return "";
        string tag = s.substr(i + 1, j - 1 - i);
        for (char ch : tag) {
            if (ch < 'A' || 'Z' < ch) return "";
        }
        i = j + 1;
        return tag;
    }

    bool validContent(string s, int& i) {
        int j = i;
        while (j < s.size()) {
            if (!validText(s, j) && !validCData(s, j) && !validTag(s, j)) break;
        }
        i = j;
        return true;
    }

    bool validText(string s, int& i) {
        int j = i;
        while (i < s.size() && s[i] != '<') { i++; }
        return i != j;
    }

    bool validCData(string s, int& i) {
        if (s.find("<![CDATA[", i) != i) return false;
        int j = s.find("]]>", i);
        if (j == string::npos) return false;
        i = j + 3;
        return true;
    }
};