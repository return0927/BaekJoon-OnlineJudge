#include <cstdio>

using namespace std;

int main() {
    int h, m, mins;
    scanf("%d %d", &h, &m);

    mins = h * 60 + m - 45;
    mins += mins >= 0 ? 0 : 1440;
    printf("%d %d", mins/60, mins%60);

    return 0;
}