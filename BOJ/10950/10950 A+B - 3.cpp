#include <cstdio>

using namespace std;

int main() {
    int a, m, n;
    scanf("%d", &a);

    for(int i=0; i<a; i++) {
        scanf("%d %d", &m, &n);
        printf("%d\n", m+n);
    }

    return 0;
}