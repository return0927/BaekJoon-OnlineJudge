#include <cstdio>

using namespace std;

int main() {
    int a;
    scanf("%d", &a);

    switch(a/10) {
        case 10:
            printf("A");
            break;
        case 9:
            printf("A");
            break;
        case 8:
            printf("B");
            break;
        case 7:
            printf("C");
            break;
        case 6:
            printf("D");
            break;
        default:
            printf("F");
    }

    return 0;
}