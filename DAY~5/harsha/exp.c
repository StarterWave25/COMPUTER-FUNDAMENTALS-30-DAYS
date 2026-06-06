#include <stdio.h>
#include <unistd.h>

int main()
{
    long long int ar[100000] = {0};
    for (int i = 0; i < 100000; i += 100)
    {
        ar[i] = 3;
        printf("%d ", ar[i]);
    }
}