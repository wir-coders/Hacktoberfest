#include<iostream>
using namespace std;
main()
{
    int i,x,fact=1;
    cout<<"Enter the value of x: "<<endl;
    cin>>x;

    for(i=x;i>0;i--)
    {
        fact*=i;
    }
    cout<<"The factorial of "<<x<<" is "<<fact<<endl;
}
