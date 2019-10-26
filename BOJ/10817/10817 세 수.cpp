#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int arr[3] = {a, b, c};
    sort(arr, arr+3);
    printf("%d", arr[1]);

    return 0;
}