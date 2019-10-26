#include <iostream>
#include <string>

using namespace std;

int main() {
    int Tcount;
    cin >> Tcount;

    for(int i=0; i<Tcount; i++) {
        int loop;
        char S[20] = "";
        cin >> loop >> S;

        string s;
        for(char c: S) {
            if(c != 0) for(int j=0; j<loop; j++) s += c;
        }
        cout << s << "\n";
    }
}