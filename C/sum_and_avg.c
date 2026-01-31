#include <stdio.h>

// Function to calculate sum
int sum_f(int arr[], int n)
{
    int i, sum = 0;
    for (i = 0; i < n; i++)
        sum += arr[i];

    return sum;
}

// Function to calculate average
float average_f(int arr[], int n)
{
    if (n == 0)
        return 0; // safety check

    return (float)sum_f(arr, n) / n;
}

int main()
{
    int n, i;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    if (n <= 0)
    {
        printf("Invalid array size.\n");
        return 0;
    }

    int arr[n];

    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    printf("Sum of elements = %d\n", sum_f(arr, n));
    printf("Average of elements = %.2f\n", average_f(arr, n));

    return 0;
}
