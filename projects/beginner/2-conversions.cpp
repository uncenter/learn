#include <iostream>

int main()
{
    std::cout << "Pick F to convert from Fahrenheit to Celsius or C to convert from Celsius to Fahrenheit: ";
    char choice;
    std::cin >> choice;
    if (choice == 'F')
    {
        double tempf;
        std::cout << "Enter a temperature in Fahrenheit: ";
        std::cin >> tempf;
        double tempc = (tempf - 32) / 1.8;
        std::cout << "The temp is " << tempc << " degrees Celsius.\n";
    }
    else if (choice == 'C')
    {
        double tempc;
        std::cout << "Enter a temperature in Celsius: ";
        std::cin >> tempc;
        double tempf = (tempc * 1.8) + 32;
        std::cout << "The temp is " << tempf << " degrees Fahrenheit.\n";
    }
}