#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<int>());

    int answer = 0;
    for (int i = 0; i < A.size(); ++i) {
        answer += A[i] * B[i];
    }

    return answer;
}

int main() {
    cout << solution({1, 4, 2}, {5, 4, 4}) << endl;
    cout << solution({1, 2}, {3, 4}) << endl;
}