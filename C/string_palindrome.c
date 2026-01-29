#include <stdio.h>

int isPalindrome(char str[])
{
    int i = 0, j;

    // Find length manually
    while (str[i] != '\0')
        i++;

    j = i - 1;
    i = 0;

    while (i < j)
    {
        // Skip spaces
        if (str[i] == ' ')
        {
            i++;
            continue;
        }
        if (str[j] == ' ')
        {
            j--;
            continue;
        }

        char left = str[i];
        char right = str[j];

        // Convert uppercase to lowercase
        if (left >= 'A' && left <= 'Z')
            left = left + 32;
        if (right >= 'A' && right <= 'Z')
            right = right + 32;

        if (left != right)
            return 0;

        i++;
        j--;
    }

    return 1;
}

int main()
{
    char str[100];

    printf("Enter a string: ");
    scanf(" %[^\n]", str); // reads full line including spaces

    if (isPalindrome(str))
        printf("Palindrome\n");
    else
        printf("Not Palindrome\n");

    return 0;
}
