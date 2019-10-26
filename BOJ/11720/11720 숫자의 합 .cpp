#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, count=0;
    cin >> n;

    char s[100] = {0};
    scanf(" %s", s);

    for(int i=0; i<n; i++) {
        count += (s[i] - '0');
    }
    cout << count;

    return 0;
}