#include <stdio.h>
int main(){
    int x, y;
    scanf("%d %d", &x, &y);
    while (1){
        if (x == 1){
            printf("POSSIBLE\n");
            return 0;
        }
        else if (x * y == 0){
            printf("IMPOSSIBLE\n");
            return 0;
        }
        else if (y == 1){
            printf("POSSIBLE\n");
            return 0;
        }
        else if (x >= y) x %= y;
        else y %= x;
    }
    return 0;
}
