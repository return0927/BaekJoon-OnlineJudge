#include <cstdio>

using namespace std;

bool t(int a, int b) {return !(bool)(a%b);}

int main() {
    int a;
    scanf("%d", &a);
    printf("%d", (bool)(t(a, 4) && (!t(a, 100) || t(a, 400))));

    return 0;
}