#include<iostream>
using namespace std;
int main()
{
	int a[100],n,mid,val;
	int beg,end;
	cout<<"enter the size: ";
	cin>>n;
	cout<<"enter the elements: \n";
	for(beg=0;beg<n;beg++)
	{
		cin>>a[beg];
	}
	cout<<"enter the value to be found: ";
	cin>>val;

	mid=(n-1)/2;
	beg=0;
	end=n-1;
	while(1)
	{
		if(a[mid]==val)
		{
			cout<<"found at "<<mid+1;
			exit(0);
		}
		else if(val<a[mid])
		{
			end=mid-1;
			mid=(beg+end)/2;
		}
		else if(val>a[mid])
		{
			beg=mid+1;
			mid=(beg+end)/2;
		}
		else if(beg>n)
		{
			cout<<"not found";
			exit(0);
		}
		else 
		cout<<"error";
	}
	return 0;
}
