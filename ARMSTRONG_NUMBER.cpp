//write a progrom to Check Armstrong Number (4 digit)
//My Code for HackToberFest

#include <iostream.h>
#include<conio.h>
#include<math.h>
int main()
{
clrscr();
cout<<"Created By denis"<<endl;
float n,m,s=0,b,count=0;
cout<<"enter the number to find ";
cin>>n;
b=n;
while(n){
      n=n/10;
      count++;
  }
  
while(n>0)
{
m=n%10;
s=s+pow(m,count);
n=n/10;
}


if(b==s)
cout<<" amstrong number is"<<b;
else
cout<<"not amstrong";
getch();
return 0;
}

