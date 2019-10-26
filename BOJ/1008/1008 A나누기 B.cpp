#include <cstdio>

using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);  // scanf_s를 쓰려고 했는데 BaekJoon에서 No scope 오류를 낸다..
    printf("%.9f", (double)a /(double)b);
    return 0;
}