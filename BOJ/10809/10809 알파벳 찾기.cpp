#include <iostream>
#include <string>

using namespace std;

int main() {
    char s[100] = "";
    int temp;
    int count[(int)'z' - (int)'a' + 1];
    fill_n(count, (int)'z' - (int)'a' + 1, -1);

    scanf("%s", s);


    for(int i=0; i<100; i++) {
        temp = (int)s[i] - (int)'a';
        if(count[temp] == -1) count[temp] = i;
    }

    for(int i: count) cout << i << " ";

    return 0;
}