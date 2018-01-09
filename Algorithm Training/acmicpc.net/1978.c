#include <stdio.h>
#include <stdbool.h>
int main(){
    int n, i, j; int p_sum=0; scanf("%d", &n);
    for(i=0; i<n; i++){
        int tmp; scanf("%d", &tmp);
        bool p=1;
        for(j=2; j<tmp; j++){
            if(tmp%j==0){ p=0; break; }
        }
        if(tmp==1) p=0;
        if(p==true) p_sum++;
    }
    printf("%d", p_sum);
}
