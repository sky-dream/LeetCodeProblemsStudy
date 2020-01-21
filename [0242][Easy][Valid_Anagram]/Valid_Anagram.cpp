#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm> //used to get the sort function.
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if(s==t)
            return true;
        else
            return false;
    }
};
int main(){
    char str1[] = "anagram";
    char str2[] = "nagaramx";
    Solution *Solution_obj = new Solution();
    bool result = Solution_obj->isAnagram(str1, str2);
	cout << "In cpp code,result value is " << ((result == false)?"FALSE":"TRUE")<< '\n';
    return 0;
}