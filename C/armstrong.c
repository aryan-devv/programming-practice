#include <stdio.h>

// Function to calculate power manually
int power(int base, int exp)
{
    int result = 1;
    for (int i = 1; i <= exp; i++)
        result *= base;
    return result;
}

// Function to check Armstrong number
int isArmstrong(int num)
{
    int original = num;
    int digit, sum = 0;
    int count = 0;
    int temp = num;

    // Special case for 0
    if (num == 0)
        return 1;

    // Count digits
    while (temp != 0)
    {
        count++;
        temp /= 10;
    }

    temp = num;

    // Calculate Armstrong sum
    while (temp != 0)
    {
        digit = temp % 10;
        sum += power(digit, count);
        temp /= 10;
    }

    return (sum == original);
}

int main()
{
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (isArmstrong(num))
        printf("%d is an Armstrong number\n", num);
    else
        printf("%d is not an Armstrong number\n", num);

    return 0;
}
