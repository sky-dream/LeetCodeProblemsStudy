int subtractProductAndSum(int n){
    int multi = 1,sum = 0;
    while(n){
        multi  = n%10 * multi;
        sum  = n%10 + sum;
        n = n/10;
    }
    return (multi - sum);
}