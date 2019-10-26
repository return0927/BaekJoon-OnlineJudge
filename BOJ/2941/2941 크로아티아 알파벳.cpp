#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string replace_all(string &str, const string& from, const string& to) {
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length();
    }
    return str;
}


int main() {
    string s;
    getline(cin, s);

    s = replace_all(s, "c=", "_");
    s = replace_all(s, "c-", "_");
    s = replace_all(s, "dz=", "_");
    s = replace_all(s, "d-", "_");
    s = replace_all(s, "lj", "_");
    s = replace_all(s, "nj", "_");
    s = replace_all(s, "s=", "_");
    s = replace_all(s, "z=", "_");
    cout << s.size();

}