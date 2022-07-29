#include "iostream"
#include "vector"

using namespace std;

int main() {
    long long a, b, c = 0;
    cin >> a;
    cin >> b;
    cin >> c;

    string time = to_string(a * b * c);

    vector<long long> v(10);
    for (int i = 0; i < time.length(); ++i) v[(time[i] - '0')] += 1;
    for (int i = 0; i < v.size(); ++i) cout << v[i] << endl;
}