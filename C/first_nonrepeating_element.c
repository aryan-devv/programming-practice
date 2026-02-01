#include <stdio.h>

// Function to find first non-repeating element
int firstNonRepeating(int arr[], int n)
{
    int i, j, count;

    for (i = 0; i < n; i++)
    {
        count = 0;

        for (j = 0; j < n; j++)
        {
            if (arr[i] == arr[j])
            {
                count++;
            }
        }

        if (count == 1)
        {
            return arr[i]; // first non-repeating element
        }
    }

    return -1; // if no non-repeating element exists
}

int main()
{
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter array elements: ");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    int result = firstNonRepeating(arr, n);

    if (result != -1)
        printf("First non-repeating element: %d", result);
    else
        printf("No non-repeating element found");

    return 0;
}
