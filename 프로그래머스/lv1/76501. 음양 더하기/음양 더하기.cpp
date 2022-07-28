#include "iostream"
#include "vector"

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;

    for (int i = 0; i < absolutes.size(); ++i) {
        if (signs[i]) answer += absolutes[i];
        else answer -= absolutes[i];
    }
    return answer;
}

int main() {
    cout << solution({4, 7, 12}, {true, false, true}) << endl;
    cout << solution({1, 2, 3}, {false, false, true}) << endl;
}