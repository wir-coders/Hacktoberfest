#include<iostream>
using namespace std;
main()
{
    int x;
    cout<<"Enter the value of x: "<<endl;
    cin>>x;
    if(x<0)
        cout<<"The number is negative. "<<endl;
    else if(x>0)
        cout<<"The number is positive. "<<endl;
    else
        cout<<"The number is zero. "<<endl;
}
