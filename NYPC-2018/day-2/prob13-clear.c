#include <stdio.h>
void swap(int *a, int *b){
    int tmp = *a; *a = *b; *b = tmp;
}
int main(){
    int n, t;
    scanf("%d %d", &n, &t);
    int matrix[n][n];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++)
            scanf("%d", &matrix[i][j]);
    }
    for (int repeat = 0; repeat < t; repeat ++){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n-1; j++){
                if (matrix[i][j] > matrix[i][j+1])
                    swap(&matrix[i][j], &matrix[i][j+1]);
            }
        }
        int rotated[n][n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++)
                rotated[i][j] = matrix[j][n - i - 1];
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++)
                matrix[i][j] = rotated[i][j];
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }
    return 0;
}
