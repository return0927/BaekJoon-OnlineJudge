#include <iostream>
#include <vector>
using namespace std;

int each_sum(int n) {
    int sum = 0;
    for(; n>0; n /= 10) {
        sum += n % 10;
    }
    return sum;
}

int main() {
    int temp;
    vector<int> selfno(10000);

    for(int i=1; i<=10000; i++) {
        temp = each_sum(i) + i;
        if(temp <= 10000) selfno[temp-1] = 1;
    }

    for(int i=0; i<10000; i++) {
        if(selfno[i] == 0) printf("%d\n", i+1);
    }

    return 0;
}