#include <stdio.h>

void rotateMatrix(int n, int mat[n][n])
{
    int i, j, temp;

    // STEP 1: Transpose the matrix
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            temp = mat[i][j];
            mat[i][j] = mat[j][i];
            mat[j][i] = temp;
        }
    }

    // STEP 2: Reverse each row
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n / 2; j++)
        {
            temp = mat[i][j];
            mat[i][j] = mat[i][n - j - 1];
            mat[i][n - j - 1] = temp;
        }
    }
}

int main()
{
    int n, i, j;

    printf("Enter matrix size: ");
    scanf("%d", &n);

    int mat[n][n];

    printf("Enter matrix elements:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &mat[i][j]);
        }
    }

    rotateMatrix(n, mat);

    printf("Matrix after 90 degree clockwise rotation:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}
