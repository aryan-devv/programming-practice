#include <stdio.h>

void digitFrequency(long long n)
{
    int freq[10] = {0};

    // Special case: number is 0
    if (n == 0)
    {
        freq[0] = 1;
    }

    // Count digits
    while (n > 0)
    {
        int digit = n % 10;
        freq[digit]++;
        n = n / 10;
    }

    // Display result
    for (int i = 0; i < 10; i++)
    {
        if (freq[i] > 0)
            printf("%d -> %d\n", i, freq[i]);
    }
}

int main()
{
    long long num;

    printf("Enter a number: ");
    scanf("%lld", &num);

    digitFrequency(num);

    return 0;
}
