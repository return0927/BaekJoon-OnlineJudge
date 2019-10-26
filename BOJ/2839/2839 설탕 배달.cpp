#include <iostream>
using namespace std;


int main() {
    int n;
    cin >> n;

    for(int k=n/5 + (n%5 != 0); k<=n/3; k++) {
        float x = (n - 3*k)/2.0;
        float y = k - x;
        if(x == (int)x && y == (int)y) {
            cout << k;
            return 0;
        }
    }
    cout << -1;

    return 0;
}