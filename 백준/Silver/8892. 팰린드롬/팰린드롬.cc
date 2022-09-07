#include "iostream"
#include "vector"
#include "algorithm"
#include "string"

using namespace std;

string palindrome() {
    int n;
    cin >> n;

    vector<string> arr;
    for (int i = 0; i < n; ++i) {
        string word;
        cin >> word;
        arr.push_back(word);
    }

    for (int i = 0; i < arr.size(); ++i) {
        for (int j = 0; j < arr.size(); ++j) {
            if (i != j) {
                string word = arr[i] + arr[j];
                string reverseWord = word;
                reverse(reverseWord.begin(), reverseWord.end());
                if (word == reverseWord) {
                    return word;
                }
            }
        }
    }
    return "0";
}

int main() {
    int t;
    cin >> t;

    while (t > 0) {
        const string ans = palindrome();
        if (ans == "0") {
            cout << 0 << endl;
        } else {
            cout << ans << endl;
        }

        t--;
    }
}