#include<iostream>

using namespace std;

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


