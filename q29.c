#include<stdio.h>
int main(void)
{
    int x;
    printf("Enter the value of x:\n");
    scanf("%d",&x);
    for(int i=1;i<=x;i++)
    {
        for(int l=i-1;l>0;l--)
        {
            printf(" ");
        }
        for(int j=i;j<=x;j++)
        {
            printf("%d",j);
        }
        printf("\n");
    }
}
