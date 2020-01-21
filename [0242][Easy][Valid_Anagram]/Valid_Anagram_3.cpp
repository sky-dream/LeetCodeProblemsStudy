#include <string.h>
#include <stdlib.h>
#include <iostream>  
//#include <algorithm> //used to get the sort function.
//#include <unordered_map>  //used to get the unordered_map variable type.
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        int num[26]={0}; 
        if(s.length()!=t.length())
            return false;
        for(int i=0;s[i]!='\0';i++){
            num[s[i]-'a']++;
            num[t[i]-'a']--;
           
        }
        for(int i=0;i<26;i++)
            if(num[i]!=0)
                return false;
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