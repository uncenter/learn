#include <iostream>

int main() 
{
    int num;
    std::cout << "Enter an integer: ";
    std::cin >> num;
    int result = 1;
    for (int i = 1; i < num + 1; i++) {
        result = result * i;
    }
    std::cout << result;
}