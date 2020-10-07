#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
int arr[4],arr1[4],arr2[4],arr3[4],i,j,bt=0;
cout<<"enter the burst time for 4 process"<<endl;
for(i=0;i<4;i++)
{
cin>>bt;
arr[i]=bt;
}
bt=0;
for(i=0;i<4;i++)
{
if(i>0)
{
arr1[i]=arr1[i-1]+arr[i-1];
}
else
{arr1[0]=0;}
}
for(i=0;i<4;i++)
{
arr2[i]=arr[i]+arr1[i];
}

cout<<"P"<<"  "<<"B.T"<<"  "<<"W.T"<<"  "<<"TAT"<<endl;
for(i=0;i<4;i++)
{
cout<<i<<"  "<<arr[i]<<"    "<<arr1[i]<<"     "<<arr2[i]<<endl;
}
cout<<"gant chart:"<<endl;
for(i=0;i<4;i++)
{cout<<"|"<<i;

for(j=0;j<arr[i];j++)
{
cout<<" ";
}
}
cout<<"|"<<endl;
for(i=0;i<4;i++)
{
cout<<arr[i];
for(j=0;j<arr[i];j++)
{
cout<<" ";
}
}
return 0;
}
