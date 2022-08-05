#include "iostream"
#include "vector"
#include "sstream"

using namespace std;

vector<string> split(string str, char Delimiter) {
    istringstream iss(str);
    string buffer;

    vector<string> result;
    while (getline(iss, buffer, Delimiter)) {
        result.push_back(buffer);
    }

    return result;
}

int main() {
    string s;
    cin >> s;

    vector<string> result = split(s, ',');
    cout << result.size() << endl;
}