#include "iostream"
#include "string"

using namespace std;

string word = "CAMBRIDGE";
string key;

int main() {
    cin >> key;

    for (int i = 0; i < key.length(); ++i) {
        // 해당 안되는 문자는 출력하자!
        // string::npos -> 탐색에 실패하면 무작위 long long 값 리턴
        // find로 리턴된 값이 string::npos와 같으면 포함 되지 않는다는 뜻
        if (word.find(key[i]) == string::npos) {
            cout << key[i] << "";
        }
    }

}