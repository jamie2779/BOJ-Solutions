// scanf와 EOF 활용
#include<stdio.h>

int main() {
    int x;
    while (scanf("%d", &x) != EOF) {
        //내부 코드
    }
    return 0;
}

//scanf가 성공적으로 입력받은 개수를 반환한다는 점 활용
#include<stdio.h>

int main() {
    int x;
    while (scanf("%d", &x) == 1) {
        //내부 코드
    }
    return 0;
}


//getchar과 EOF 활용
#include <stdio.h>

int main() {
	int x;
	while (1) {
		x = getchar();
		if (ch == EOF) {
			break;
		}
        //내부 코드
    }
	return 0;
}
