#include<iostream>
#include<cstring>

using namespace std;

//frequency of char in two string is same or not - S1 - Siva , S2 - Siva

//checking the char occurance of the both string is same or not

//Time Complexity - O(N)

bool frequency_of_chars(string S1,string S2)
{
    //declare a char count of size 256
    int count[256] = {0};
    //if length of two strings are not equal then it return false
    if(S1.length()!=S2.length())
    {
        return false;
    }
    //it traverse through the first string and count the char count
    for(int i=0;i<S1.length();i++)
    {
        count[S1[i]]++;
    }
    //it traverse through the second string and decrement the char count
    for(int j=0;j<S2.length();j++)
    {
        count[S2[j]]--;
    }

    //after decrementing all char count will be zero if it is still one then return false
    for(int k=0;k<256;k++)
    {
        if(count[k]!=0)
        {
            return false;
        }
    }
    return true;
}

int main()
{

    string s1,s2;
    cout<<"Enter the input of the first string: ";
    getline(cin,s1);
    cout<<"Enter the input of the second string: ";
    getline(cin,s2);
    int a = frequency_of_chars(s1,s2);
    cout<<a;
}
