#include<iostream>
using namespace std;
main()
{
    int i,x,y,z;
    cout<<"Enter the value of x:"<<endl;
    cin>>x;
    cout<<"Enter the value of y:"<<endl;
    cin>>y;
    if(x>y)
    {
        x=x+y;
        y=x-y;
        x=x-y;
    }
    z=x;

    for(i=z;i>0;i--)
    {
        if(x%i==0&&y%i==0)
        {
            cout<<"The Greatest common divisor(GCD) of "<<x<<" and "<<y<<" is "<<i<<"."<<endl;
            break;
        }
    }
}
