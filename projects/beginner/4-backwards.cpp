#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Enter a string: ";
    string input;
    string output = "";
    cin >> input;
    for (int i = input.length() + 1; i >= 0; i--) {
        cout << input[i];
    }
}
