#include "iostream"
#include "vector"

using namespace std;

int costumeParty(int s, vector<int> cows) {
    int cnt = 0;
    for (int i = 0; i < cows.size(); ++i) {
        for (int j = i + 1; j < cows.size(); ++j) {
            if (cows[i] + cows[j] <= s) {
                cnt++;
            }
        }
    }
    return cnt;
}


int main() {
    int n, s;
    scanf("%d %d", &n, &s);

    vector<int> cows;
    for (int i = 0; i < n; ++i) {
        int size;
        scanf("%d", &size);
        cows.push_back(size);
    }

    int cnt = costumeParty(s, cows);
    printf("%d \n", cnt);
}
