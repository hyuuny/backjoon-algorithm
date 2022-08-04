#include "iostream"

using namespace std;

int main() {
    int arr[6];
    for (int i = 0; i < 6; ++i) {
        scanf("%d", &arr[i]);
    }

    int chess[] = {1, 1, 2, 2, 2, 8};
    for (int i = 0; i < 6; ++i) {
        cout << chess[i] - arr[i] << " ";
    }

}