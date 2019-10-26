#include <cstdio>

using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);  // scanf_s를 쓰려고 했는데 BaekJoon에서 No scope 오류를 낸다..
    printf("%d\n" "%d\n" "%d\n" "%d",
            a*(b%10), a*(b/10%10), a*(b/100%10), a*b);
    return 0;
}