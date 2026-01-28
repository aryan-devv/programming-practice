#include <stdio.h>

int sum_of_digits(int n)
{
    int sum = 0;

    if (n < 0)
        n = -n;

    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }

    return sum;
}

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);

    printf("The sum of digits of %d = %d\n", n, sum_of_digits(n));
    return 0;
}
