#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int delChain(int *list, int list_idx, int *new_list, int new_idx){
  int count = 0;
  int prev = 0;
  for (int i = 0; i < list_idx+1; i++){
    if (prev != list[i]){
      if (count >= 3)
        printf("prev(%d) * %d\n", prev, count);
      else if (i != 0){
        printf("clear : %d\n", prev);
        for (int j = 0; j < count; j++){
          new_list[new_idx] = prev;
          new_idx++;
        }
      }
      count = 0;
    }
    prev = list[i];
    count++;
  }
  return new_idx;
}
int main(){
  int list_idx;
  scanf("%d", &list_idx);
  char str[list_idx];
  scanf("%s", str);
  int list[list_idx];
  for (int i = 0; i < strlen(str); i++){
    list[i] = (int)str[i];
  }
  for (int i = 0; i < list_idx; i++){
    printf("%d ", list[i]);
  }
  printf("\n");
  // ===============
  int new_list[list_idx];
  memset(new_list, 0, sizeof(new_list));
  int new_idx = 0;
  new_idx = delChain(list, list_idx, new_list, new_idx);
  for (int i = 0; i < new_idx; i++){
    printf("%d ", new_list[i]);
  }
  printf("\n");
  // ===============
  for (int i = 0; i < list_idx; i++)
    list[i] = new_list[i];
  memset(new_list, 0, sizeof(new_list));
  new_idx = 0;
  new_idx = delChain(list, list_idx, new_list, new_idx);
  for (int i = 0; i < new_idx; i++){
    printf("%d ", new_list[i]);
  }
  printf("\n");
  // ===============
  for (int i = 0; i < list_idx; i++)
    list[i] = new_list[i];
  memset(new_list, 0, sizeof(new_list));
  new_idx = 0;
  new_idx = delChain(list, list_idx, new_list, new_idx);
  for (int i = 0; i < new_idx; i++){
    printf("%c", new_list[i]);
  }
  printf("\n");
  return 0;
}
