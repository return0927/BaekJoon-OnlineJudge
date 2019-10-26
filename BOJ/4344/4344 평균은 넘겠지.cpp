#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n, m, temp, count;
    double mean, total = 0.0f;
    cin >> n;

    for(int i=0; i<n; i++) {
        cin >> m;

        vector<int> scores;
        total = 0;
        count = 0;

        for(int j = 0; j < m; j++) {
            cin >> temp;
            scores.push_back(temp);
            total += temp;
        }

        mean = (double) total / m;
        for(int s : scores) {
            if(s > mean) count++;
        }
        printf("%.3f%%\n", (double)count/m * 100);
    }

    return 0;
}