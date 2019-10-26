#include <iostream>

using namespace std;

/* int factorial2(int n) {
    if(n == 1) return 1;
    else return n*factorial2(n-1);
}

int factorial(int n) {
    return n == 1 ? 1 : n * factorial(n-1);
}*/

int main() {
    int n, total=1;
    scanf("%d", &n);

    for(int i=2;i<=n;i++) {
        total *= i;
    }
    printf("%d", total);

    return 0;
}