#include<iostream>
using namespace std;
main()
{
    int i,x,y,z;
    cout<<"Enter the value of x:"<<endl;
    cin>>x;
    cout<<"Enter the value of y:"<<endl;
    cin>>y;

    if(x<y)
    {
        x=x+y;
        y=x-y;
        x=x-y;
    }
    z=x;
    for(i=1;;i++)
    {
        z=x*i;
        if(z%x==0&&z%y==0)
        {
            cout<<"The lcm of "<<x<<" and "<<y<<" is "<<z<<"."<<endl;
            break;
        }
    }

}
