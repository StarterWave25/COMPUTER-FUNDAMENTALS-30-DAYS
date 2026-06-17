#include <unistd.h>
int main()
{
    char msg[] = "Hello System Calls\n";
    write(
        1000,
        msg,
        sizeof(msg));
    return 0;
}