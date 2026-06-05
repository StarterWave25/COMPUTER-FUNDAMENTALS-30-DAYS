#include <stdio.h>
#include <unistd.h>

int main()
{
    long long x = 0;
    while (1)
    {
        printf("%d\n", x++);
    }
}