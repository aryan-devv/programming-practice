#include <stdio.h>

int second_smallest(int arr[], int n)
{
    int smallest, second_smallest;

    if (n < 2)
    {
        printf("Array must contain at least two elements.\n");
        return -1;
    }

    // Initialize smallest and second smallest
    if (arr[0] < arr[1])
    {
        smallest = arr[0];
        second_smallest = arr[1];
    }
    else
    {
        smallest = arr[1];
        second_smallest = arr[0];
    }

    for (int i = 2; i < n; i++)
    {
        if (arr[i] < smallest)
        {
            second_smallest = smallest;
            smallest = arr[i];
        }
        else if (arr[i] < second_smallest && arr[i] != smallest)
        {
            second_smallest = arr[i];
        }
    }

    return second_smallest;
}

int main()
{
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d elements:\n", n);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    int result = second_smallest(arr, n);

    if (result != -1)
        printf("Second smallest element is: %d\n", result);

    return 0;
}
