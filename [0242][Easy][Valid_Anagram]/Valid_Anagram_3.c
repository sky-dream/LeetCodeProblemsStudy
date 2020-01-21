#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
bool isAnagram(char* s, char* t) {
    int ctr[128] = {};
    while (*s) ++ctr[*s++];
    while (*t) --ctr[*t++];
    for (int i=0; i<128; i++)
        if (ctr[i])
            return false;
    return true;
}

void main(){
    char str1[] = "anagram";
    char str2[] = "nagaram";
    bool result = isAnagram(str1, str2);
    printf("In c code,result value is %s",result==false?"FALSE":"TRUE");
}