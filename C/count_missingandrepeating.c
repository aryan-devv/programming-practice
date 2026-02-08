#include <stdio.h>

int main()
{
    int n;

    // Take size of array
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n]; // dynamic-sized array (VLA)

    // Take array elements
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    int missing = -1;
    int repeating = -1;

    // Check numbers from 1 to n
    for (int i = 1; i <= n; i++)
    {
        int count = 0;

        // Count how many times i appears
        for (int j = 0; j < n; j++)
        {
            if (arr[j] == i)
            {
                count++;
            }
        }

        if (count == 0)
            missing = i;

        if (count == 2)
            repeating = i;
    }

    printf("Repeating Number: %d\n", repeating);
    printf("Missing Number: %d\n", missing);

    return 0;
}
