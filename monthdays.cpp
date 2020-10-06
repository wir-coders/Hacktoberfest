#include<iostream>
using namespace std;
main()
{
    int days,years,months,weeks;
    cout<<"Enter the number of days: "<<endl;
    cin>>days;
    years=days/365;
    days%=365;
    months=days/30;
    days%=30;
    weeks=days/7;
    days%=7;
    cout<<"The number of years are "<<years<<"."<<endl;
    cout<<"The number of months are "<<months<<"."<<endl;
    cout<<"The number of weeks are "<<weeks<<"."<<endl;
    cout<<"The number of days are "<<days<<"."<<endl;

}
