#include <iostream>
#include <string>

using namespace std;

int main() {
    int total = 0, time[] = {11, 2, 3, 4, 5, 6, 7, 8, 9, 10},
        match[] = {2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9};
    string s;
    cin >> s;

    for(char c : s) {
        total += time[match[(int)c - (int)'A']];
    }
    cout << total;
}