#include <stdio.h>

int main()
{
    int n;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    int found = 0;

    for (int i = 0; i < n; i++)
    {
        int leftSum = 0, rightSum = 0;

        // Sum of elements before index i
        for (int j = 0; j < i; j++)
        {
            leftSum += arr[j];
        }

        // Sum of elements after index i
        for (int j = i + 1; j < n; j++)
        {
            rightSum += arr[j];
        }

        if (leftSum == rightSum)
        {
            printf("Equilibrium index found at: %d\n", i);
            found = 1;
            break;
        }
    }

    if (!found)
    {
        printf("No equilibrium index found.\n");
    }

    return 0;
}
