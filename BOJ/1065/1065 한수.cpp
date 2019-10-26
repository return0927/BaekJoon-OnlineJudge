#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> split(int n) {
    vector<int> result;

    for(; n > 0; n /= 10) {
        result.push_back(n % 10);
    }
    reverse(result.begin(), result.end());
    return result;
}

vector<int> delta(vector<int> vec) {
    vector<int> result;
    for(auto it = vec.begin() + 1; it != vec.end(); it++) {
        result.push_back(*it - *(it - 1));
    }
    return result;
}

vector<int> set(vector<int> vec) {
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
    return vec;
}

int main() {
    int n, count=0;
    cin >> n;

    for(int i=1; i<=n; i++) {
        if(i < 10) {
            count++;
            continue;
        } else {
            auto r = set(delta(split(i)));
            count += r.size() == 1 ? 1 : 0;
        }
    }
    cout << count;

    return 0;
}