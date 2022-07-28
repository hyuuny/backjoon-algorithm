#include "iostream"

using namespace std;
string s = "";
int zero_cnt, one_cnt = 0;

void init() {
    if (s[0] == '1') zero_cnt++; else one_cnt++;
}

void flip() {
    for (int i = 0; i < s.length() - 1; ++i) {
        if (s[i] != s[i + 1]) {
            if (s[i + 1] == '1') zero_cnt++; else one_cnt++;
        }
    }
}

int main() {
    cin >> s;
    init();
    flip();
    cout << min(zero_cnt, one_cnt);
}