#include <stdio.h>

int checkNumber(int n)
{
    if (n > 0)
        return 1;
    else if (n < 0)
        return -1;
    else
        return 0;
}

int main()
{
    int n, result;

    printf("Enter a number: ");
    scanf("%d", &n);

    result = checkNumber(n);

    if (result == 1)
        printf("The number is Positive.\n");
    else if (result == -1)
        printf("The number is Negative.\n");
    else
        printf("The number is Zero.\n");

    return 0;
}
