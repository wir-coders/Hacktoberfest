/* Balanced Tree has a height of LogN */
#include <iostream>
#include <queue>
using namespace std;
class node{
public:
	int data;
	node* left;
	node* right;

	node(int d)
	{
		data = d;
		left = NULL;
		right = NULL;
	}
};

void bfs(node* root){
	queue<node*> q;
	q.push(root);
	q.push(NULL);
	while(!q.empty()){
		node* f = q.front();

		if(f==NULL){
			cout << endl;
			q.pop();
			if(!q.empty()){
				q.push(NULL);
			}
		}
		else{
			cout << f->data << ", ";
			q.pop();
			if(f->left){
				q.push(f->left);
			}
			if(f->right){
				q.push(f->right);
			}
		}
	}
}

node* buildTreeFromArray(int ar[], int s, int e){
	// Base Case
	if(s>e){
		return NULL;
	}
	int mid = (s+e)/2;
	node* root = new node(ar[mid]);
	root->left = buildTreeFromArray(ar,s,mid-1);
	root->right = buildTreeFromArray(ar,mid+1,e);
	return root;
}
int main(){
	
	int ar[]= {1,2,3,4,5,6,7};
	int n = sizeof(ar)/sizeof(n);
	node* root = buildTreeFromArray(ar,0,n-1);

	bfs(root);


	return 0;
}