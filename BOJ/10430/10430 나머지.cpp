#include <cstdio>

using namespace std;

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);  // scanf_s를 쓰려고 했는데 BaekJoon에서 No scope 오류를 낸다..
    printf("%d\n%d\n%d\n%d", (a+b)%c, (a%c + b%c)%c, (a*b)%c, (a%c * b%c)%c);
    return 0;
}