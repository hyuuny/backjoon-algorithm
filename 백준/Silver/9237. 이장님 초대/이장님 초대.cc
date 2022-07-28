#include "iostream"
#include "vector"
#include "algorithm"

using namespace std;

vector<int> generateTree(int n) {
    vector<int> v;
    for (int i = 0; i < n; ++i) {
        int tree;
        cin >> tree;
        v.push_back(tree);
    }
    // 내림차순 정렬
    sort(v.rbegin(), v.rend());
    return v;
}

int calculateDay(vector<int> &v, int n) {
    int day = 0;
    for (int i = 0; i < n; ++i) day = max(day, v[i] + (i + 1) + 1);
    return day;
}

int main() {
    int n;
    cin >> n;

    vector<int> v = generateTree(n);
    int max_day = calculateDay(v, n);
    cout << max_day << endl;
}