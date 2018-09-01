#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    int n;
    scanf("%d", &n);
    int login[n];
    memset(login, 0, n);
    int logout[n];
    memset(login, 0, n);
    for (int i = 0; i < n; i++){
        int in_h, in_m, out_h, out_m;
        scanf("%2d:%2d %2d:%2d", &in_h, &in_m, &out_h, &out_m);
        login[i] = in_h*60 + in_m;
        logout[i] = out_h*60 + out_m;
    }
    int logged_in[2000];
    memset(logged_in, 0, 2000);
    int logged_in_idx = 0;
    // len(logged_in) -> logged_in_idx + 1
    int tmp_range[2000];
    memset(tmp_range, 0, 2000);
    int tmp_range_idx = 0;
    int tmp_hot[2000];
    memset(tmp_hot, 0, 2000);
    int tmp_hot_idx = 0;
    int cache = 0;
    for (int time_now = 0; time_now < 1440; time_now++){
        for (int i = 0; i < n; i++){
            if (login[i] == time_now){
                logged_in[logged_in_idx] = i;
                logged_in_idx++;
            }
            if (logout[i] == time_now){
                int idx = 0;
                for (int j = 0; j<logged_in_idx+1; j++){
                    if (logged_in[j] == i){
                        idx = j;
                        break;
                    }
                }
                for(int j = idx; j < logged_in_idx+1; j++)
                    logged_in[j] = logged_in[j + 1];
            }
        }
        if (cache != sizeof(logged_in)){
            tmp_hot[tmp_hot_idx] = logged_in_idx + 1;
            tmp_hot_idx++;
            tmp_range[tmp_range_idx] = time_now;
            tmp_range_idx++;
        }
        cache = sizeof(logged_in_idx + 1);
    }
    int max = tmp_hot[0]; 
    int idx = 0;
    for (int i = 1; i < tmp_hot_idx+1; i++){
        if (tmp_hot[i] > max){
            max = tmp_hot[i];
            idx = i+1;
        }
    }
    printf("%d\n", tmp_hot[idx]);
    printf("%02d:%02d ", tmp_range[idx]/60, tmp_range[idx]%60);
    printf("%02d:%02d\n", tmp_range[idx+1]/60, tmp_range[idx+1]%60);
    return 0;
}
