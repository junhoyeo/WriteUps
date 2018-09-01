#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

struct Event {
    int x;
    int y;
    int t;
};

int cmp_event(const void *a, const void *b) {
    struct Event *e1 = a;
    struct Event *e2 = b;
    return (e1->t > e2->t) - (e1->t < e2->t);
}

int cmp_int(void* a, void* b){
    return (*(int*)a - *(int*)b);
}

bool in(int val, int *arr){
    for (int i = 0; i < sizeof(arr); i++) {
        if (arr[i] == val) return true;
    }
    return false;
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    int infected[n];
    memset(infected, 0, n);
    infected[0] = 1;
    int infected_idx = 1;
    struct Event events[m];
    memset(events, 0, sizeof(events));
    for (int i = 0; i<m; i++)
        scanf("%d %d %d", &events[i].x, &events[i].y, &events[i].t);
    qsort(events, m, sizeof(struct Event), cmp_event);
    for (int i = 0; i<m; i++){
        bool inf_x = in(events[i].x, infected);
        bool inf_y = in(events[i].y, infected);
        if (inf_x && inf_y) continue;
        if (inf_x && !inf_y){
            infected[infected_idx] = events[i].y;
            infected_idx++;
        }
        if (!inf_x && inf_y){
            infected[infected_idx] = events[i].x;
            infected_idx++;
        }
    }
    qsort(infected, infected_idx, sizeof(int), cmp_int);
    for (int i = 0; i<infected_idx; i++)
        printf("%d ", infected[i]);
    printf("\n");
    return 0;
}
