/**
    Contributed By: Adit Shah
    Algorithm to find k-th smallest array-element without actual sorting (Array size:n and 1 <= k <= n)
    (i.e. k=1 gives the smallest element of the array and k=n gives the largest)
    Time Complexity: O(n)
**/
#include<bits/stdc++.h>
using namespace std;
float k_smallest(float [],int,int,int,int);     // Function that finds the k-th smallest element as per given criteria of k being 0 < k <n+1
float selection(float [],int,int,int,int);      // Function to find element that will be present at the kth index if the array is sorted, so range of k in this case is 0 <= k <= n-1
int Partition(float [],int,int,float);         // Function that partitions the array w.r.t to the given pivot
int main()
{
    int n,k;

    //User Input
    cout<<"Enter the size of the input list: ";
    cin>>n;         //size of our input list
    cout<<"\n";
    float arr[n];
    for(int i=0;i<n;i++){
        cout<<"Enter "<<i+1<<" element : ";
        cin>>arr[i];
    }
    cout<<"\nIf you want to find the k-th smallest element, enter k :";
    cin>>k;

    //Displaying the Output
    cout<<"\nThe k-th smallest element in the given list is: "<<k_smallest(arr,0,n,n,k)<<endl;
    return 0;
}
// This function normalizes the value of k and r to give input to the selection function and then ultimately returns the answer to the main function
// For this function, l is inclusive but r is not, also 0 < k < n+1
float k_smallest(float p[],int l,int r,int n,int k)
{
    return selection(p,l,r-1,n,k-1);
}
// Function to find element that will be present at the kth index if the array is sorted, so range of k in this case is 0 <= k <= n-1 as k represents index here instead of rank
float selection(float p[],int l,int r,int n,int k)    // l and r both are inclusive, 0 <= k < n
{
    if(n<5)         // Base case when group(s) of 5 can not be formed
    {
        sort(p+l,p+l+n);       // This sort will not take n*log(n) time as we are sorting <5 elements
        return(p[l+k]);
    }
    else
    {
        // grouping the elements into groups of 5 thereby forming a 2-D array 'a' of order [n/5] X 5
        float a[n/5][5];
        for(int k=0;k<n/5;k++)
            for(int i=0;i<5;i++)
            {
                a[k][i]=p[l+5*k+i];
            }

        // Constructing array b containing median of each group created above after each group of 5 is sorted
        float b[n/5];
        for(int i=0;i<n/5;i++)
        {
            sort(a[i],a[i]+5);       // This sort will not take n*log(n) time as we are sorting just 5 elements at a time
            b[i]=a[i][2];
        }

        // Recursive call to find the median of medians
        float x=selection(b,0,n/5-1,n/5,n/10);

        // Appropriate recursive calls made to find the element which will be positioned at index k(function parameter) had the array been sorted
        int q=Partition(p,l,r,x);
        int n1=q-l;     //Number of elements to the left of partition index q
        int n2=r-q;     //Number of elements to the right of the partition index q
        if(q==k)        // if we require the element at index q only (i.e if k=q) then p[q]=x should be returned
            return x;
        else if(q>k)    // if q>k, recursive call to be made on the the left side of q (Divide n conquer)
            return selection(p,0,q-1,n1,k);
        else            // if q<k, recursive call to be made on the the right side of q and now the index we want in this sub-array will become k-q-1 instead of k (Divide n conquer)
            return selection(p,q+1,r,n2,k-q-1);
    }
}

// Function that partitions the array w.r.t to a given pivot
int Partition(float A[],int l,int r,float p)  // l and r both are inclusive so for full array take l=0 and r=n-1
{
    int t;                  // to find index of element p
    for(int i=l;i<=r;i++)
        if(A[i]==p)
            t=i;        //found index of element p
    swap(A[t],A[r]);
    int i=l-1;
    for(int j=l;j<=r-1;j++)
    {
        if(A[j]<=A[r])
        {
            i++;
            swap(A[i],A[j]);
        }
    }
    swap(A[i+1],A[r]);
    return (i+1);
}
/** -------------------------END OF THE CODE ----------------------------------------- **/
