#include <iostream>
#include <cmath>

double normalize(double signal)
{
    return signal / 100.0;
}

double noise(double signal)
{
    return log(signal + 1);
}

int main()
{
    double s;

    while(std::cin >> s)
    {
        std::cout << normalize(s) << " "
                  << noise(s) << std::endl;
    }

    return 0;
}