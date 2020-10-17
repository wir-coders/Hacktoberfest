 
#include <bits/stdc++.h>
using namespace std;
 

bool isSafe(vector<vector<int>> &v, int i,int j){

    for(int x=0;x<i;x++){
        if(v[x][j]==1)
            return false;
    }

    int x = i;
    int y = j;

    while(x>=0 && y>=0){
        if(v[x][y]==1)
            return false;
        x--;
        y--;
    }

    x= i;
    y=j;
    while(x>=0 && y<v.size()){
        if(v[x][y]==1)
            return false;
        x--;
        y++;
    }
    return true;
}


bool solveNqueens(vector<vector<int>> &v, int index){

    if(index == v.size()){
        
        for(int i=0;i<v.size();i++){
            for(int j =0;j<v.size();j++){
                if(v[i][j]==1)
                    cout<<"Q"<<" ";
                else
                    cout<<"_"<<" ";
            }
            cout<<endl;
        }

        cout<<endl<<endl;
        return false;
    }

    for(int j=0;j<v.size();j++){

        if(isSafe(v,index,j)){

            // putting queen on i,j 
            v[index][j] =1;

            // trying to put queen in the next row;
            bool isValidMove  = solveNqueens(v,index+1);

            // if this move is valid then retun true;
            if(isValidMove){
                return true;
            }

            // Means i,j is not the right path so backtrack;
            v[index][j]=0;
        }
    }
    // Now we have checked all the possible arrangements and there is no way to put queen
    // so return false;
    return false;
 }


int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    
    int n;
    cin>>n;
    vector<vector<int>> board(n,vector<int>(n,0));

    solveNqueens(board,0);
} 


Q _ _ _ _ 
// _ _ Q _ _ 
// _ _ _ _ Q 
// _ Q _ _ _ 
// _ _ _ Q _ 


// Q _ _ _ _ 
// _ _ _ Q _ 
// _ Q _ _ _ 
// _ _ _ _ Q 
// _ _ Q _ _ 


// _ Q _ _ _ 
// _ _ _ Q _ 
// Q _ _ _ _ 
// _ _ Q _ _ 
// _ _ _ _ Q 


// _ Q _ _ _ 
// _ _ _ _ Q 
// _ _ Q _ _ 
// Q _ _ _ _ 
// _ _ _ Q _ 


// _ _ Q _ _ 
// Q _ _ _ _ 
// _ _ _ Q _ 
// _ Q _ _ _ 
// _ _ _ _ Q 


// _ _ Q _ _ 
// _ _ _ _ Q 
// _ Q _ _ _ 
// _ _ _ Q _ 
// Q _ _ _ _ 


// _ _ _ Q _ 
// Q _ _ _ _ 
// _ _ Q _ _ 
// _ _ _ _ Q 
// _ Q _ _ _ 


// _ _ _ Q _ 
// _ Q _ _ _ 
// _ _ _ _ Q 
// _ _ Q _ _ 
// Q _ _ _ _ 


// _ _ _ _ Q 
// _ Q _ _ _ 
// _ _ _ Q _ 
// Q _ _ _ _ 
// _ _ Q _ _ 


// _ _ _ _ Q 
// _ _ Q _ _ 
// Q _ _ _ _ 
// _ _ _ Q _ 
// _ Q _ _ _ 

