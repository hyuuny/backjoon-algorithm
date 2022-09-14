#include "algorithm"
#include "string"

using namespace std;

long long solution(long long n) {
    string ans = to_string(n);
    std::sort(ans.begin(), ans.end(), greater<>());
    return atoll(ans.c_str());
}

int main() {
    printf("%lld", solution(118372));
}