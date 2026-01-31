#include <stdio.h>

void findMinMax(int arr[], int n, int *min, int *max)
{
    int i;
    *min = *max = arr[0];

    for (i = 1; i < n; i++)
    {
        if (arr[i] > *max)
            *max = arr[i];
        else if (arr[i] < *min)
            *min = arr[i];
    }
}

int main()
{
    int n, i, min, max;

    printf("Enter the number of elements: ");
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

    findMinMax(arr, n, &min, &max);

    printf("Maximum element = %d\n", max);
    printf("Minimum element = %d\n", min);

    return 0;
}
