#include<stdio.h>
int main(void)
{
    int x;
    printf("Enter the value of x:\n");
    scanf("%d",&x);
    for(int i=x;i>=1;i--)
    {
        for(int l=x-i;l>0;l--)
        {
            printf(" ");
        }
        for(int j=1;j<=i;j++)
        {
            printf("%d",j);
        }
        printf("\n");
    }
}
