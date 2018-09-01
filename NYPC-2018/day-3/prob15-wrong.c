#include <stdio.h>
#include <string.h>
#include <stdbool.h>

struct Point { 
    int x; int y;
};

int n;

bool in(struct Point val, struct Point *arr){
    for (int i = 0; i < sizeof(arr); i++) {
        if ((arr[i].x == val.x) && arr[i].y == val.y)
            return true;
    }
    return false;
}

void cluster(struct Point ret[], int ret_idx, int grid[n][n]) {
    int col = grid[0][0];
    struct Point stack[n*n];
    memset(stack, 0, sizeof(stack));
    int stack_idx = 0;
    stack[stack_idx].x = 0;
    stack[stack_idx].y = 0;
    stack_idx++;
    while (sizeof(stack) > 0){
        struct Point curr = stack[stack_idx];
        stack[stack_idx].x = 0;
        stack[stack_idx].y = 0;
        stack_idx--;
        ret[ret_idx] = curr;
        ret_idx++;
        int c_x = curr.x;
        int c_y = curr.y;
        struct Point nbs[4] = {0,};
        nbs[0].x = c_x;
        nbs[0].y = c_y + 1;
        nbs[1].x = c_x;
        nbs[1].y = c_y - 1;
        nbs[2].x = c_x + 1;
        nbs[2].y = c_y;
        nbs[3].x = c_x - 1;
        nbs[3].y = c_y;
        for (int i = 0; i < 4; i++){
            if ((nbs[i].x < n) && (nbs[i].x >= 0) && (nbs[i].y < n) && (nbs[i].y >= 0)){
                if ((grid[nbs[i].x][nbs[i].y] == col) && (!in(nbs[i], ret))){
                    stack[stack_idx].x = nbs[i].x;
                    stack[stack_idx].y = nbs[i].y;
                    stack_idx++;
                }
            }
        }
    }
}

int main(){
    int k;
    scanf("%d %d", &n, &k);
    int colors[k];
    if (k != 0){
        for (int i = 0; i < k; i++)
            scanf("%d", &colors[i]);
    }
    int grid[n][n];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++)
            scanf("%d", &grid[i][j]);
    }
    for (int i = 0; i < k; i++){
        struct Point points[n*n];
        int points_idx = 0;
        cluster(points, points_idx, grid);
        for (int j = 0; j < points_idx; j ++){
            grid[points[j].y][points[j].x] = colors[i];
        }
    }
    struct Point points[n*n];
    int points_idx = 0;    
    cluster(points, points_idx, grid);
    printf("%d", points_idx);
    return 0;
}
