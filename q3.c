#include<stdio.h>
int main(void)
{
    int x;
    printf("Enter the value of x:\n");
    scanf("%d",&x);
    printf("\n\n");
    for(int i=1;i<=x;i++)
    {
        for(int j=1;j<=i;j++)
        {
            printf("%d",i);
        }
        printf("\n");
    }
}
