bool isValid(char* s) {
    
    int len = strlen(s);
    printf("input string |%s| length is |%d|\n", s, len);
    if (len == 0) {
                return true;
            }
    //for a char array or a string in c or cpp code, it always ends up with an end character "\0",
    //for string "0123", we need char str[5], not char str[4] to finish the copy strcpy(str,"0123"); 

    // if use below malloc(),  there will be heap buffer overload when do printf("%s",temp),need check why calloc is ok?
    //char *temp = (char *)malloc(sizeof(char)*(len+1)/2); 

    //malloc will not init the requested heap memory, but calloc will do that.          
    char *temp = (char *)calloc(((len+1)/2+1),sizeof(char));

    int p = 0;
    for (int i = 0; i < len; i++) {
        
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            temp[p]= s[i];
            p++;
        }
        else {
            //the first char must start with left tag char, 
            if (p == 0) {
                free(temp);
                return false;
            }           
            if ((s[i] == ')' && temp[p-1] != '(') || (s[i] == ']' && temp[p-1] != '[') || (s[i] == '}' && temp[p-1] != '{')) {
                free(temp);
                return false;
            } else {
                temp[p-1] = '\0';
                p--;
            }
            }
        // the number of left matching char must not bigger than half of the input string length.  
        if( (p > (len+1)/2) ){
            printf("p > (len+1)/2, return false,\n");
            free(temp);
            return false;
            }          
        printf("value of p is %d,\n",p);
        printf("temp string is >%s< , length is  %d \n", temp, strlen(temp));
    } 
    //if right tags are matching with left tags, then the number of temp should be reduced to 0 when the loop comes to the end.     
    bool result = (strlen(temp) == 0);
    free(temp); 
    return  result;
}