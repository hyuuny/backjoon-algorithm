#include "iostream"

using namespace std;

int calculateFatigue(int a, int b, int c, int m){
    int hour = 24;
    int fatigue = 0;
    int maxJob = 0;

    while (hour > 0) {
        hour--;

        // 쌓일 피로도가 최대 피로도보다 작으면 일을 할 수 없음.
        if (a > m) break;

        // 일하면 쌓일 피로도가 최대 피로도보다 크면 쉬면서 c만큼 피로도를 줄이자.
        if (fatigue + a > m) {
            // 피로도 음수는 0 처리
            if (fatigue - c <= 0) fatigue = 0;
            else fatigue -= c;
        } else {
            // 일 할 수 있으니까 일하자!
            fatigue += a;
            maxJob += b;
        }
    }
    return maxJob;
}

int main() {
    int a, b, c, m;
    cin >> a >> b >> c >> m;
    cout << calculateFatigue(a, b, c, m) << endl;
}