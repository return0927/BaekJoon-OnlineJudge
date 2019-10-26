#include <iostream>
using namespace std;

int counter(int N) {
    int n=0, count=1;

    N = (N-2)/6 + 1;

    do {
        n += count++;
    } while(n < N);
    return count;
}


int main() {
    int N;
    cin >> N;

    if(N == 1) {
        cout << 1;
        return 0;
    }
    cout << counter(N);
}