#include "iostream"
#include "algorithm"

using namespace std;

int h[1000], a[1000];

void initArr(int arr[], int len) {
    for (int i = 0; i < len; ++i)
        scanf("%d", &arr[i]);
}

int main() {
    int n, m;
    cin >> n >> m;

    initArr(h, n);
    initArr(a, m);

    int maxH = *max_element(h, h + n);
    int maxA = *max_element(a, a + m);

    cout << maxH + maxA << endl;
}