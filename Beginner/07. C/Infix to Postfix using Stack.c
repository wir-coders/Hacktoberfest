#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int n=0;
int p=-1;
char *s;
void push(char c)
{
    p++;
    s[p]=c;
}
char pop()
{
    if(p==-1)
        return -1;
    p--;
    return s[p+1];
}

int op_find(char a)
{
    switch(a)
    {
        case '+':
        case '-':
            return 0;
        case '/':
        case '*':
            return 1;
        case '^':
            return 2;
    }
    return -1;
}
int main()
{
    printf("Enter the infix expression:");
    char string[100];
    fgets(string,100,stdin);
    n=strlen(string);
    s=(char*)malloc(n*sizeof(char));
    char res[n];
    int c=0;
    for(int i=0;i<n;i++)
    {
        if(op_find(string[i])!=-1)
        {
            while(p!=-1 && op_find(s[p])>=op_find(string[i]))
            {
                res[c]=pop();
                c++;
            }
            push(string[i]);
        }
        else if(string[i]=='(')
                push('(');
        else if(string[i]==')')
        {
            while(s[p]!='(')
            {
                res[c]=pop();
                c++;
            }
            char t=pop();
        }
        else
        {
            res[c]=string[i];
            c++;
        }
    }
    while(p!=-1)
        res[c++]=pop();
    printf("Postfix expression would be: ");
    for(int i=0;i<c;i++)
        printf("%c",res[i]);
    return 0;
}
