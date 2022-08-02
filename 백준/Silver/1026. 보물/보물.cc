#include "iostream"
#include "vector"
#include "algorithm"

using namespace std;

void inputVector(vector<int> &v, int n) {
    while (n > 0) {
        int num;
        cin >> num;
        v.push_back(num);
        n--;
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> a, b;
    inputVector(a, n);
    inputVector(b, n);

    sort(a.begin(), a.end());
    sort(b.rbegin(), b.rend());
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += a[i] * b[i];
    }

    cout << ans << endl;
}