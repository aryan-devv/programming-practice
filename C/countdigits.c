#include <stdio.h>

int count_digit(int n)
{
    int count = 0;

    if (n == 0)
        return 1;

    if (n < 0)
        n = -n; // convert to positive

    while (n > 0)
    {
        n /= 10;
        count++;
    }

    return count;
}

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);

    printf("There are %d digits in %d\n", count_digit(n), n);
    return 0;
}
