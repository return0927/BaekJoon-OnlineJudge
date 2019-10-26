#include <iostream>

using namespace std;

int main() {
    int a, max=0, index=-1;

    for(int i=1; i<=9; i++) {
        cin >> a;
        if(a > max) {
            max = a;
            index = i;
        }
    }

    cout << max << "\n" << index;

    return 0;
}