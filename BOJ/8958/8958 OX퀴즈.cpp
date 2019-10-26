#include <iostream>
#include <string>
using namespace std;


int main() {
    int n;
    string s;

    cin >> n;
    for(int i=0; i<n; i++) {
        int now = 0, total = 0;
        cin >> s;

        for(char c : s) {
            if(c == 'O') {
                now += 1;
            } else {
                total += now*(now+1)/2;
                now = 0;
            }
        }
        total += now*(now+1)/2;
        cout << total << "\n";
    }


    return 0;
}