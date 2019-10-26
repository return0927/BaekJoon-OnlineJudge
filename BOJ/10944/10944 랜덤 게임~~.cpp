#include <iostream>
#include <random>

using namespace std;

int main() {
    random_device rd;
    mt19937_64 rnd(rd());

    uniform_int_distribution<int> range(1, 10000);
    printf("%d", range(rnd));

    return 0;
}