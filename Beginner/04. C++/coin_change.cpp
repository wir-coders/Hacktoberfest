
// Dynamic Pogramming coin change problem

#include<bits/stdc++.h>
using namespace std;

int changeTopDown(vector<int> a, int total,int i){
	if(total == 0){
		return 1;
	}
	if(total < 0){
		return 0;
	}
	if(total >= 1 and i<=0){
		return 0;
	}

	return changeTopDown(a,total-a[i-1],i) + changeTopDown(a,total,i-1);

}

int bottomUp(vector<int> a, int amount){
	vector<int> dp(amount+1);
	dp[0] = 1;
	for(auto coin : a){
		for(int amt = 1; amt<=amount; amt++){
			if(amt >= coin){
				dp[amt] += dp[amt-coin];
			}
		}
	}

	return dp[amount];
}


int main(){
	int n;
	cin>>n;
	vector<int> a(n); //coins array
	for(int i = 0; i < n; i++){
		cin>>a[i];
	}
	int coin;
	cin>>coin;
	cout<<changeTopDown(a,coin,n)<<endl;
	cout<<bottomUp(a,coin);
}
