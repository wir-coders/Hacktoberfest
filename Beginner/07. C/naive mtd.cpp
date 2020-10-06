

#include<iostream> 
#include<climits> 


using namespace std; 
  
int Find_maxSubarraySum(int a[], int size) 
{ 
    int max = INT_MIN, max_end = 0; 
  
    //here for each element we are finding the maximum value and calculating the sums of those elements
    for (int i = 0; i < size; i++) 
    { 
        max_end = max_end + a[i]; 
        if (max < max_end) 
            max = max_end; 
  
        if (max_end < 0) 
            max_end = 0; 
    } 
    return max; 
} 
  

int main() 
{ 

//initializing the array
    int a[] = {-10,-13,23,-10,-11,8,13,-17}; 
    //calculating the size of the given array
    int n = sizeof(a)/sizeof(a[0]); 
    //here Find_maxSubarraySum() returns the maximum sum for the max_sum variable
    int max_sum = Find_maxSubarraySum(a, n); 
    cout << "Maximum subarray sum is " << max_sum; 
    return 0; 
} 

