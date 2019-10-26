#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<string> set(vector<string> vec) {
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
    return vec;
}

int main() {
    int n, count=0;
    cin >> n;

    for(int i=0; i<n; i++) {
        bool yes = true;
        string s;
        cin >> s;

        vector<char> letters(s.begin(), s.end());
        vector<char> set_letters;

        for(char c : letters) {
            if(set_letters.empty() || set_letters.back() != c) {
                if(find(set_letters.begin(), set_letters.end(), c) != set_letters.end()) {
                    yes = false;
                    break;
                }
                set_letters.push_back(c);
            }
        }
        if(yes) count++;
    }
    cout << count;

    return 0;
}