#include <iostream>
using namespace std;
class node {
public:
	int data;
	node* next;

	// constructor
	node(int d)
	{
		data = d;
		next = NULL;
	}
};
node* midpointLL(node*head)
{
	if(head==NULL || head->next==NULL)
	{
		return head;
	}
	
	node* fast = head->next;
	node* slow = head;
	while(fast->next!=NULL && fast!=NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return slow;
}
node* merge(node* a, node* b)
{
	if(a==NULL)
		return b;
	else if(b==NULL)
		return a;

	node* c;
	// Comparing a and b for smaller 
	if(a->data < b->data)
	{
		c = a;
		c->next = merge(a->next,b);
	} 
	else
	{
		c = b;
		c->next = merge(a,b->next);
	}
	return c;

}
node* mergeSort(node* head)
{
	// Base Case
	if(head==NULL || head->next==NULL)
	{
		return head;
	}
	// Rec Case
	node* mid = midpointLL(head);
	node* a = head;
	node* b = mid->next;

	mid->next = NULL;         // breaking the link in the List 

	a = mergeSort(a);
	b = mergeSort(b);

	node* c = merge(a,b);
	return c;

}
void insertAtTail(node* &head, int data)
{
	if(head==NULL)
	{
		head = new node(data);
		return;
	}
	node* tail = head;
	while(tail->next!=NULL)
	{
		tail = tail->next;
	}
	tail->next = new node(data);
	return;
}
void buildList(node* &head)
{
	int data;
	cin >> data;             // Input data till user enters -1
	while(data!=-1)
	{
		insertAtTail(head,data);
		cin >> data;
	}
}
void printList(node*head)          
{
	while(head!=NULL)
	{
		cout << head->data << " ";
		head = head->next;
	}
	cout << endl;
}
int main()
{
	// Enter the data of the array..
	node* head1 = NULL;
	buildList(head1);
	printList(head1);
	node* head = mergeSort(head1);
	printList(head); 
}