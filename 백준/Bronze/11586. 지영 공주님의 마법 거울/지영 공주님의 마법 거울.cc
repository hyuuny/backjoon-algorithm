#include "iostream"
#include "vector"

using namespace std;

void currentPrint(vector<string> v) {
    for (int i = 0; i < v.size(); i++) { cout << v[i] << endl; }
}

void inversionPrint(vector<string> v) {
    for (int i = 0; i < v.size(); i++) {
        for (int j = v[i].size() - 1; j >= 0; j--) {
            if (j == 0) {
                cout << v[i][j] << endl;
            } else {
                cout << v[i][j];
            }
        }
    }
}

void reversePrint(vector<string> v) {
    for (int i = v.size() - 1; i >= 0; i--) { cout << v[i] << endl; }
}

int n;
vector<string> v;

int main() {
    cin >> n;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        v.push_back(s);
    }

    int k;
    cin >> k;
    if (k == 1) { currentPrint(v); }
    if (k == 2) { inversionPrint(v); }
    if (k == 3) { reversePrint(v); }

}