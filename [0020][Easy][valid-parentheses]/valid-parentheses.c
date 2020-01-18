bool isValid(char* s) {
    
    int len = strlen(s);
    if (len == 0) {
                return true;
            }
    char *temp = malloc(sizeof(char)*(len+1));
    int p = 0;
    
    for (int i = 0; i < len; i++) {
        
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            temp[p] = s[i];
            p++;
        } else {
            if (p == 0) {
                return false;
            } else {
                if ((s[i] == ')' && temp[p-1] != '(') || (s[i] == ']' && temp[p-1] != '[') || (s[i] == '}' && temp[p-1] != '{')) {
                    return false;
                } else {
                    temp[p-1] = '\0';
                    p--;
                }
            }
        }
    }
    
    return strlen(temp) == 0;
}