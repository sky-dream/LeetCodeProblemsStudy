// leetcode time     cost : 0 ms
// leetcode memory   cost : 5.9 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
void reverse(char *s, int start, int end) {
    char temp;
    while (start < end) {
        temp = s[start];
        s[start++] = s[end];
        s[end--] = temp;
    }
}

void trimSpace(char *s, int start) {
    // 将中间多余的空格移到最后，同时把字符串结束符\0向前搬一个
    do {
        s[start] = s[start+1];
        start++;
    } while (s[start]);  // 在字符串结束符停止
}

char * reverseWords(char * s){
    // 1.消除前面多余空格
    while (*s == ' ') s++;
    // 2.消除后面的空格，且长度-1
    int len = strlen(s) - 1;
    if (len < 0) return s;
    while (s[len] == ' ') {
        s[len] = '\0';
        len--;
    }
    reverse(s, 0, len);  // 整体翻转

    // 3.消除中间多余空格并反转局部
    int i, idx = 0;
    for (i = 0; s[i] != '\0'; i++) {
        if (s[i] == ' ') {  // 遇到空格表示单词结束
            reverse(s, idx, i - 1);  // 注意区间[idx,i-1]是单词
            // 准备删除第二个空格
            while (s[i+1] && s[i+1] == ' ') {
                trimSpace(s, i + 1);
                len--;  // 修改字符数组长度
            }
            idx = i + 1;  // 最后idx移到新的单词开头这里
        }
    }
    // 处理最后单词
    reverse(s, idx, len);
    return s;
}