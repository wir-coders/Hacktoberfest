#include<bits/stdc++.h>
using namespace std;
int main(){
int a;
cout<<"Enter the number of Rows in the pyramid\n";
cin>>a;
for(int j=0;j<a;j++)
{
for(int i=0;i<j;i++){
cout<<i;
}
cout<<"\n";
}
return 0;
}
