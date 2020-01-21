#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
bool isAnagram(char *s, char *t)
{
	int i, x[26] = { 0 }, y[26] = { 0 };
	for (i = 0; s[i] != '\0'; i++)	x[s[i] - 'a']++;	//建立 s 的字符表 x
	for (i = 0; t[i] != '\0'; i++)	y[t[i] - 'a']++;	//建立 t 的字符表 y
	for (i = 0; i < 26; i++)							//比较两字符表是否相同
		if (x[i] != y[i])	return false;
	return true;										//种类、个数均相同
}

void main(){
    char str1[] = "anagram";
    char str2[] = "nagaram";
    bool result = isAnagram(str1, str2);
    printf("In c code,result value is %s",result==false?"FALSE":"TRUE");
}