#include <stdio.h>
int main()
{
    int pre = 1, cur = 1, temp, i, n;
    printf("Enter a number");
    scanf("%d", &n);
    printf("0\t%d\t%d", pre, cur);
    for (i = 3; i <= n; i++)
    {
        temp = cur;
        cur = pre + cur;
        pre = temp;
        printf("\t%d", cur);
    }
}
