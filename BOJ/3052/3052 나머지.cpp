#include <iostream>
using namespace std;


int main() {
    int n, total = 0, count[42] = {0, };

    for(int i=0; i<10; i++) {
        cin >> n;
        if(count[n%42] == 0) total += 1;
        count[n%42] += 1;
    }

    cout << total;

    return 0;
}