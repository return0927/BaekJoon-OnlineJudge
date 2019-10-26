#include <iostream>
using namespace std;


int main() {
    int A, B, C,
        count[10] = {0, };

    cin >> A;
    cin >> B;
    cin >> C;

    A *= B * C;
    for(; A>0; A /= 10) {
        count[A%10] += 1;
    }
    for(int i: count) {
        cout << i << "\n";
    }

    return 0;
}