#include<stdio.h>
#include<string.h>
int main()
{
    int n;
    int k;
    printf("ENTER THE LENGTH OF THE ARRAY------------------------------------->");
    scanf("%d",&n);
    int arr[n],answer[n];
    printf("ENTER THE ELEMENTS OF THE ARRAY SEPRATED BY A SPACE---> ");
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("ENTER THE MAXIMUM ELEMENT OF THE ARRAY WHICH U WANT TO BE SORTED-->");
    scanf("%d",&k);
    int count[k+1];
    for(int i=0;i<k+1;i++)
        count[i]=0;
    for(int i=0;i<n;i++)
        count[arr[i]]++;
    for(int i=1;i<=k;i++)
        count[i] += count[i-1];
    for(int i=n-1;i>=0;i--)
        answer[--count[arr[i]]]=arr[i];
    for(int i=0;i<n;i++)
        printf("%d",answer[i]);
    return 0;
}