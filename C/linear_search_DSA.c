#include <stdio.h>

/*
    Function: linearSearch
    ----------------------
    Searches for a target element in an array using Linear Search.

    arr[]  : input array
    n      : number of elements in array
    target : element to be searched

    returns:
        index of target if found
        -1 if not found
*/
int linearSearch(int arr[], int n, int target)
{
    // Traverse the array one element at a time
    for (int i = 0; i < n; i++)
    {
        // Check if current element matches the target
        if (arr[i] == target)
        {
            // Target found → return its index immediately
            return i;
        }
    }

    // If loop completes, target was not found
    return -1;
}

int main()
{
    int n, target;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter element to search: ");
    scanf("%d", &target);

    int result = linearSearch(arr, n, target);

    if (result != -1)
    {
        printf("Element found at index %d\n", result);
    }
    else
    {
        printf("Element not found\n");
    }

    return 0;
}
