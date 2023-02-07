#include<iostream>
#include<string>
#include<unordered_map>

using namespace std;

int main()
{
    string letters = "abcdefghijklmnopqrstuvwxyz";
    string input;
    cout << "Enter a string: ";
    cin >> input;
    unordered_map<char, int> freq;
    for (int i = 0; i < input.length(); i++) {
        char c = input[i];
        if (freq.count(c)) {
            freq[c] += 1;
        } else {
            freq[c] = 1;
        }
    }
    cout << "{";
    int i = 0;
    for (auto it : freq) {
        if (i == 0) {
            cout << it.first << ":" << it.second;
        } else  {
            cout << ", " << it.first << ":" << it.second;
        }
        i ++;
    }
    cout << "}";


}
