#include <cstdio>

using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);  // scanf_s�� ������ �ߴµ� BaekJoon���� No scope ������ ����..
    printf("%d\n%d\n%d\n%d\n%d", a+b, a-b, a*b, a/b, a%b);
    return 0;
}