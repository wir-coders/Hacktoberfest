#include<iostream>

using namespace std;

// for arithmetic  progression there will a starting number , common difference and ending number

// AP = a+d till n;

//Time Complexity - O(N)

int main()
{
    int N;
    cout<<"Enter the value of N: ";
    cin>>N;
    int starting_number = 2;
    int common_difference = 2;
    for(int i=0;i<N;i++)
    {
        cout <<starting_number<<" ";
        starting_number = starting_number + common_difference;
    }
    return 0;

}


