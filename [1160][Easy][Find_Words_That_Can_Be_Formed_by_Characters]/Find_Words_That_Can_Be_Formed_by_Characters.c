// leetcode time     cost : 32 ms
// leetcode memory   cost : 8.3 MB 
int countCharacters(char ** words, int wordsSize, char * chars){
    int nums = strlen(chars);
    if (wordsSize == 0 || nums == 0) return 0;  //一者为空直接出局
    int max = 0, j = 0;
    int map[26], count[26]; //hash表 与 计数数组
    memset(map, 0, sizeof(map)); //hash表初始化
    for (int c = 0; c < nums; c++) { //生成hash值
        map[chars[c] - 'a']++;
    }
    for (int i = 0; i < wordsSize; i++) {
        int len = strlen(words[i]);
        if (len > nums) continue;  //单个word长度超过字母表长度，无效
        memset(count, 0, sizeof(count)); //计数数组归零
        for (j = 0; j < len; j++) {
            if (map[words[i][j] - 'a'] <= count[words[i][j] - 'a']) break; //hash值为0 或 重复字母不足
            count[words[i][j] - 'a']++;  //计数+1，代表字母重复一次
        }
        if (j == len) max += len; //当上面循环有break存在时，无效
    }
    return max;
}