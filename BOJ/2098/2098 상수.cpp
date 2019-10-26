#include <iostream>
#include <string>

using namespace std;

int reverse(int a) {
    string s;

    for(; a>0; a /= 10) {
        s += to_string(a%10);
    }
    return stoi(s);
}

int main() {
    int a, b;
    cin >> a >> b;

    a = reverse(a);
    b = reverse(b);

    printf("%d", a > b ? a : b);

    return 0;
}