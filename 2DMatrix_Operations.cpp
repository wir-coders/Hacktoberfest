//Operations on 2D Matrix
//Contributed by Toshani 
#include <iostream>
using namespace std;
void swap (int ar[10][10], int row, int col);
void div_mul (int ar[10][10], int row, int col);
void dia (int ar[10][10], int row, int col);
int c, r, i, j;
int main ()
{
	int a[10][10];
	char choice;
	do 
    {
    	a[0][0]=0;
	    cout<<"Enter the no of rows and columns for the matrix \n\n";
	    cin>>r>>c;
	    cout<<"Enter the values of the matrix \n\n";
	    for( i=0;i<r;i++)
	    {
		    for( j=0;j<c;j++)
		    {
			    cin>>a[i][j];
		    }
    	}
	    cout<<"The enetered matrix is:\n";
	    for( i=0;i<r;i++)
	    {
		    for( j=0;j<c;j++)
		    {
			    cout<<a[i][j]<<"\t";
		    }
		    cout<<"\n";
	    }
	    int ch;
	    cout<<"Enter your choice\n";
	    cout<<"1:Swap columns\n";
	    cout<<"2:Divide or multiply\n";
	    cout<<"3:Lower half of diagonals\n";
	    cin>>ch;
	    switch (ch)
	    {
	        case 1:swap(a,r,c);
	        break;
	        case 2:div_mul(a,r,c);
	        break;
	        case 3:dia(a,r,c);
	        break;
	        default:"Invalid entry";
        }
        cout<<"\nDo you want  to continue? \t";
        cin>>choice;
	}while (choice=='y' or choice=='Y');
}

void swap (int ar[10][10], int row, int col)
{
	int temp = 0;
	for (int i=0; i<row; i++)
	{
		temp = ar[i][0];
		ar[i][0] = ar[i][col-1];
		ar[i][col-1] = temp;
	}
	cout<<"The new array is: \n";
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			cout<<ar[i][j]<<"\t";
		}
		cout<<"\n";
	}
}

void div_mul (int ar[10][10], int row, int col)
{
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			if ((ar[i][j]%5)==0)
			{
				ar[i][j] = (ar[i][j])/5;
			}
			else 
			{
				ar[i][j] = (ar[i][j])*2;
			}
		}
	}
	cout<<"The new array is: \n";
	for (int i=0; i<row; i++)
	{
		for (int j = 0; j<col; j++)
		{
			cout<<ar[i][j]<<"\t";
		}
		cout<<"\n";
	}
}

void dia (int ar[10][10], int row, int col)
{
	for (int i=0; i<r; i++)
	{
		for (int j=0; j<=i; j++)
		{
			cout<<ar[i][j]<<"\t";
		}
		cout<<"\n";
	}
}