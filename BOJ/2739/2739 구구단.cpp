#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int a;
    scanf("%d", &a);

    for(int i=1; i<10; i++) printf("%d * %d = %d\n", a, i, a*i);

    return 0;
}