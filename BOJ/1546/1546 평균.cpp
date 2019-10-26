#include <iostream>
using namespace std;


int main() {
    int n;
    double t, sum = 0, max = -1;

    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> t;
        sum += t;

        if(t > max) max = t;
    }
    printf("%.3f", (double)(sum / n / max * 100));

    return 0;
}