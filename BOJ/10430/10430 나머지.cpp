#include <cstdio>

using namespace std;

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);  // scanf_s�� ������ �ߴµ� BaekJoon���� No scope ������ ����..
    printf("%d\n%d\n%d\n%d", (a+b)%c, (a%c + b%c)%c, (a*b)%c, (a%c * b%c)%c);
    return 0;
}