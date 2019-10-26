#include <iostream>

using namespace std;

int main() {
    int n, t, c=1;
    cin >> n;

    t = n % 10 * 10 + (n % 10 + n / 10)%10;
    while(n != t) {
        t = t % 10 * 10 + (t % 10 + t / 10)%10;
        c++;
    }
    cout << c;

    return 0;
}