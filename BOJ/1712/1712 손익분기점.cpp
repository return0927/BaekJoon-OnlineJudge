#include <iostream>
#include <string>
using namespace std;


int main() {
    int a, b, c;
    cin >> a >> b >> c;

    printf("%d", c <= b ? -1 : a/(c-b) + 1);

    return 0;
}