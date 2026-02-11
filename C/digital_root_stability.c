#include <stdio.h>

// Function to calculate digital root and count steps
int digitalRoot(int num, int *steps)
{
    int sum, digit;
    *steps = 0;

    while (num >= 10)  // Continue until single digit
    {
        sum = 0;
        while (num > 0)
        {
            digit = num % 10;
            sum += digit;
            num /= 10;
        }
        num = sum;
        (*steps)++;  // Count step
    }

    return num;
}

int main()
{
    int number, steps, root;

    printf("Enter a positive integer: ");
    scanf("%d", &number);

    if (number < 0)
    {
        printf("Invalid input! Please enter a positive number.\n");
        return 0;
    }

    if (number == 0)
    {
        printf("Digital Root: 0\n");
        printf("This number is Stable.\n");
        return 0;
    }

    root = digitalRoot(number, &steps);

    printf("\nDigital Root: %d\n", root);
    printf("Steps Taken: %d\n", steps);

    if (steps == 1)
        printf("Status: Stable 🔹\n");
    else if (steps == 2)
        printf("Status: Semi-Stable 🔸\n");
    else
        printf("Status: Unstable 🔥\n");

    return 0;
}