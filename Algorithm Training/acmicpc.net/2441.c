#include <stdio.h>
int main(){
    int n, i, j; scanf("%d", &n);
    for(i=n; i>0; i--){
        for(j=n-i; j>0; j--) printf(" ");
        for(j=0; j<i; j++) printf("*");
        printf("\n");
    }
}
