#include <iostream>
#include <string>

using namespace std;

int main()
{
    string letters = "abcdefghijklmnopqrstuvwxyz";
    string vowels = "aeiou";
    string input;
    cout << "Enter a string: ";
    cin >> input;
    int vowel = 0;
    int consonant = 0;
    for (int i = 0; i < input.length(); i++)
    {
        if (letters.find(input[i]) != string::npos)
        {
            if (vowels.find(input[i]) != string::npos){
                vowel ++;
            } else {
                consonant ++;
            }
        }
    }
    cout << "In the given string, there are " << vowel << " vowels and " << consonant << " consonants.";
}
