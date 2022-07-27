#include "iostream"
#include "vector"
#include "algorithm"

using namespace std;

int n, k;
vector<int> v;
int cnt = 0;

int main() {
    cin >> n >> k;

    for (int i = 0; i < n; ++i) {
        int money;
        cin >> money;
        v.push_back(money);
    }

    std::reverse(v.begin(), v.end());
    for (int i = 0; i < v.size(); ++i) {
        cnt += k / v[i];
        k %= v[i];
    }

    cout << cnt << endl;
}