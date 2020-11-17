
// Graph topological sort algorithm

#include<bits/stdc++.h>
using namespace std;


void topSortUtil(int v, bool visited[], stack<int> &Stack, vector<vector<int> > graph){
	visited[v] = true;

	for(int i = 0; i < graph[v].size(); i++){
		if(visited[graph[v][i]] == false){
			topSortUtil(graph[v][i],visited,Stack,graph);
		}
	}

	Stack.push(v);

}

void topSort(vector<vector<int> > graph, int V, int E){
	stack<int> Stack;
	bool *visited  = new bool[V];
	for(int i = 0; i < V; i++){
		visited[i] = false;
	}

	for(int i = 0; i < V; i++){
		if(visited[i] == false){
			topSortUtil(i,visited,Stack,graph);
		}
	}

	// prine ordewr

	while(Stack.empty() == false){
		cout<<Stack.top()<<" ";
		Stack.pop();
	}
}



int main(){
	int V;cin>>V;
	int E;cin>>E;
	vector<vector<int> > graph(V);
	for(int i = 0; i < E; i++){
		int u;cin>>u;
		int v;cin>>v;
		graph[u].push_back(v);
	}
	topSort(graph,V,E);
}
