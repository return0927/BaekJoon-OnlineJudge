#include <cstdio>

using namespace std;

int main() {
    int a, m, n;
    scanf("%d", &a);

    for(int i=1; i<=a; i++) {
        scanf("%d %d", &m, &n);
        printf("Case #%d: %d + %d = %d\n", i, m, n, m+n);
    }

    return 0;
}