#include <iostream>
#include <vector>
using namespace std;

long long sum(vector<int> &a) {
    long long ans = 0;
    for(auto & it : a) {
        ans += it;
    }
    return ans;
}

int main() {
    vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cout << sum(test);

    return 0;
}