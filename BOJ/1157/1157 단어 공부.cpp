#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    string s;
    int count[26] = {0};
    cin >> s;

    for(char c : s) {
        if((int)c < 97) c = (char)((int)c + 32);
        //cout << c << "\n";
        count[(int)c - 97] += 1;
    }

    auto amax = max_element(count, count+26);
    auto max = *amax;
    //for(int i: count) cout << i << " ";
    //cout << "\n";
    count[amax - count] = 0;

    //for(int i: count) cout << i << " ";
    auto amax2 = max_element(count, count+26);
    auto max2 = *amax2;

    // cout << amax - count + 65 << "(" << max << ") / Next " << count - amax2 + 65<< "(" << max2 << ")";

    if(max == max2) {
        printf("?");
        return 0;
    }
    else {
        cout << (char)(amax - count + 65);
    }
}