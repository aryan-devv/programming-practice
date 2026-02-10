#include <stdio.h>

int main()
{
    long long n;
    int digits[20];
    int len = 0;

    // User prompt
    printf("Enter a positive number: ");
    scanf("%lld", &n);

    // Special case: if number is 0
    if (n == 0)
    {
        printf("Compressed output: 10\n");
        return 0;
    }

    // Store digits in reverse order
    while (n > 0)
    {
        digits[len] = n % 10;
        len++;
        n = n / 10;
    }

    // Compress and print result
    printf("Compressed output: ");

    int count = 1;
    for (int i = len - 1; i >= 0; i--)
    {
        if (i > 0 && digits[i] == digits[i - 1])
        {
            count++;
        }
        else
        {
            printf("%d%d", count, digits[i]);
            count = 1;
        }
    }

    printf("\n");
    return 0;
}
