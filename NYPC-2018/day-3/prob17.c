#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int delChain(int *list, int list_idx, int *new_list, int new_idx){
  int count = 0;
  int prev = 0;
  for (int i = 0; i < list_idx+1; i++){
    if (prev != list[i]){
      if (!(count >= 3) && i != 0){
        // printf("clear : %d\n", prev);
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
bool arraySame(int *list1, int *list2, int size){
  for (int i = 0; i < size; i++){
    if (list1[i] != list2[i]) return false;
  }
  return true;
}
int main(){
  int list_idx;
  scanf("%d", &list_idx);
  char str[list_idx];
  scanf("%s", str);
  int list[list_idx];
  for (int i = 0; i < strlen(str); i++)
    list[i] = (int)str[i];
  int new_list[list_idx];
  int new_idx = 0;
  int prev_list[list_idx];
  memset(prev_list, 0, sizeof(prev_list));
  int combo = 0;
  for(int j = 0; j < 5; j++){
    memset(new_list, 0, sizeof(new_list));
    new_idx = 0;
    new_idx = delChain(list, list_idx, new_list, new_idx);
    for (int i = 0; i < list_idx; i++)
      list[i] = new_list[i];
    if (arraySame(prev_list, list, list_idx))
      break;
    for (int i = 0; i < list_idx; i++)
      prev_list[i] = list[i];
    combo++;
  }
  printf("%d\n", combo);
  if (new_idx <= 0)
    printf("PERFECT!!!\n");
  else {
    for (int i = 0; i < new_idx; i++)
      printf("%c", new_list[i]);
    printf("\n");
  }
  return 0;
}