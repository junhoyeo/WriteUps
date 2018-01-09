#include <stdio.h>
int zero, one;
int fibonacci(int n) {
    if (n==0) {
        zero++;
        return 0;
    } else if (n==1) {
        one++;
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
int main(){
    int t, i; scanf("%d", &t);
    for(i=0; i<t; i++){
        zero=0, one=0;
        int n; scanf("%d", &n);
        fibonacci(n); printf("%d %d\n", zero, one);
    }
    return 0;
}
