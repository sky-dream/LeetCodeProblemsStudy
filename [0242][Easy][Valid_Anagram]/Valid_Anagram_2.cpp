#include <string.h>
#include <stdlib.h>
#include <iostream> 
//#include <algorithm> //used to get the sort function. 
#include <unordered_map>  //used to get the unordered_map variable type.
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> map;
        if (s.size() != t.size()) 
            return false;
        for(int i=0;i<s.size();i++){
            ++map[s[i]];
            --map[t[i]];
        }  
        for(unordered_map<char,int>::iterator it=map.begin();it!=map.end();it++){
            if(it->second!=0)
                return false;
        }
        return true;
        
    }
};
int main(){
    char str1[] = "anagram";
    char str2[] = "nagaram";
    Solution *Solution_obj = new Solution();
    bool result = Solution_obj->isAnagram(str1, str2);
	cout << "In cpp code,result value is " << ((result == false)?"FALSE":"TRUE")<< '\n';
    return 0;
}