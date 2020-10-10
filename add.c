#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
        char x[100000],y[100000];
        scanf("%s %s",x,y);
        int n1[100000]={},n2[100000]={},ans[100001]={};
        printf("%d",n1[0]);
        for(int i=0;i<strlen(x);i++)
                n1[100000-i-1]=(int)(x[strlen(x)-i-1]-48);
        for(int i=0;i<strlen(y);i++)
                n2[100000-i-1]=(int)(y[strlen(y)-i-1]-48);
        int A;
        strlen(x)>strlen(y)?(A=strlen(x)):(A=strlen(y));
        int j=100000;
        int c=0;
        for(int k=0;k<=A;k++){
                c=c+n1[j-k-1]+n2[j-k-1];
                ans[j-k]=c%10;
                c=c/10;
        }
        if(ans[100000-A]==0){
                for(int k=A-1;k>=0;k--)
                        printf("%d",ans[100000-k]);
        }
        else{
                for(int k=A;k>=0;k--)
                        printf("%d",ans[100000-k]);
        }
        return 0;
}
