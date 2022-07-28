#include "iostream"

using namespace std;

void changeBalls(int m, int basket[]) {
    for (int i = 0; i < m; ++i) {
        int a, b, c;
        cin >> a >> b >> c;

        for (int j = a; j <= b; ++j) basket[j - 1] = c;
    }
}

void printBalls(int n, int basket[]) {
    for (int i = 0; i < n; ++i) {
        cout << basket[i] << " ";
    }
}

int main() {

    int n, m;
    cin >> n >> m;

    int basket[n];
    std::fill_n(basket, n, 0);

    changeBalls(m, basket);
    printBalls(n, basket);
}