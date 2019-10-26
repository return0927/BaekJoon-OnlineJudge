#include <iostream>
using namespace std;


int main() {
    int delta, before, n;

    cin >> n;
    before = n;

    cin >> n;
    delta = n - before;
    before = n;

    for(int i=2; i<8; i++) {
        cin >> n;
        if(delta != n - before) {
            printf("mixed");
            return 0;
        }
        delta = n - before;
        before = n;
    }

    if(delta == 1) printf("ascending");
    else printf("descending");

    return 0;
}