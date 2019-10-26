#include <iostream>

using namespace std;

int main() {
    int n, a, max=-1000000, min=1000000;
    cin >> n;

    for(int i=0; i<n; i++) {
        cin >> a;
        if(a > max) max = a;
        if(a < min) min = a;
    }
    cout << min << " " << max;
    
    return 0;
}