#include<iostream>
using namespace std;
main()
{
    int year;
    cout<<"Enter the year to check whether the year is a leap year or not: "<<endl;
    cin>>year;
    if(year%4==0)
    {
        cout<<"The year is a leap year. "<<endl;
    }
    else
    {
        cout<<"The year is not a leap year."<<endl;
    }
}
