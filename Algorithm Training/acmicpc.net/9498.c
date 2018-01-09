/*시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F*/
#include <stdio.h>
int main(){
    int n; scanf("%d", &n);
    if(n>89) printf("A");
    else if(n>79) printf("B");
    else if(n>69) printf("C");
    else if(n>59) printf("D");
    else printf("F");
}
//친절하게 위에 주석이 달린 이유는 저거 새벽에 몰폰하면서 했기 때문임... 흑흑 그래서 문제기억이 안나서 같다붙인것ㅋㅋ
