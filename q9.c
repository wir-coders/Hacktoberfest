#include<stdio.h>
int main(void)
{
    int x;
    printf("Enter the value of x:\n");
    scanf("%d",&x);
    for(int i=x;i>=1;i--)
    {
        for(int j=i;j<=x;j++)
        {
            printf("%d",j);
        }
        printf("\n");
    }
}
