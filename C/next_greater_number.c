#include <stdio.h>
#include <string.h>

// Function to swap two characters
void swap(char *a, char *b)
{
    char temp = *a;
    *a = *b;
    *b = temp;
}

// Function to sort characters in ascending order
void sort(char str[], int start, int len)
{
    int i, j;
    for (i = start; i < len - 1; i++)
    {
        for (j = i + 1; j < len; j++)
        {
            if (str[i] > str[j])
                swap(&str[i], &str[j]);
        }
    }
}

int main()
{
    char num[100];
    int i, j, len, found = 0;

    printf("Enter a number: ");
    scanf("%s", num);

    len = strlen(num);

    // Step 1: Find first decreasing digit from right
    for (i = len - 2; i >= 0; i--)
    {
        if (num[i] < num[i + 1])
        {
            found = 1;
            break;
        }
    }

    if (!found)
    {
        printf("No greater permutation possible.\n");
        return 0;
    }

    // Step 2: Find smallest digit greater than num[i] to the right
    int smallest = i + 1;
    for (j = i + 1; j < len; j++)
    {
        if (num[j] > num[i] && num[j] <= num[smallest])
            smallest = j;
    }

    // Step 3: Swap
    swap(&num[i], &num[smallest]);

    // Step 4: Sort remaining digits
    sort(num, i + 1, len);

    printf("Next greater permutation: %s\n", num);

    return 0;
}
