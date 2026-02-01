#include <stdio.h>

// Function to check if two arrays are equal
int areArraysEqual(int arr1[], int arr2[], int n)
{
    int visited[n];
    int i, j, count1, count2;

    // Initialize visited array
    for (i = 0; i < n; i++)
    {
        visited[i] = 0;
    }

    for (i = 0; i < n; i++)
    {
        if (visited[i] == 1)
            continue;

        count1 = 0;
        count2 = 0;

        // Count frequency in arr1
        for (j = 0; j < n; j++)
        {
            if (arr1[i] == arr1[j])
                count1++;
        }

        // Count frequency in arr2
        for (j = 0; j < n; j++)
        {
            if (arr1[i] == arr2[j])
                count2++;
        }

        if (count1 != count2)
            return 0; // Not equal

        visited[i] = 1;
    }

    return 1; // Arrays are equal
}

int main()
{
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr1[n], arr2[n];

    printf("Enter elements of first array: ");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr1[i]);
    }

    printf("Enter elements of second array: ");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr2[i]);
    }

    if (areArraysEqual(arr1, arr2, n))
        printf("Arrays are EQUAL");
    else
        printf("Arrays are NOT equal");

    return 0;
}
