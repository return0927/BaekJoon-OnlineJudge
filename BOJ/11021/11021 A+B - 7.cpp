#include <cstdio>

using namespace std;

int main() {
    int a, m, n;
    scanf("%d", &a);

    for(int i=1; i<=a; i++) {
        scanf("%d %d", &m, &n);
        printf("Case #%d: %d\n", i, m+n);
    }

    return 0;
}