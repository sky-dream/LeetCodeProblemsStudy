#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
bool isAnagram(char * s, char * t){
    int alpha[26] = {0};
    while(*s && *t)
    {
        alpha[*s - 'a']++;
        alpha[*t - 'a']--;
        s++, t++;
    }
    if(*s || *t)
        return false;
    for(int i = 0; i < 26; ++i)
        if(alpha[i])
            return false;
    return true;
}

void main(){
    char str1[] = "anagram";
    char str2[] = "nagaram";
    bool result = isAnagram(str1, str2);
    printf("In c code,result value is %s",result==false?"FALSE":"TRUE");
}