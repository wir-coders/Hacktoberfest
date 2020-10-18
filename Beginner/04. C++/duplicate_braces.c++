//Problem Statement:
//Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.

//Check whether A has redundant braces or not.

//Return 1 if A has redundant braces, else return 0.

//Note: A will be always a valid expression.

//Sample Input 1:

//"((a + b))"

//Sample Output 1:
//1
//Sample Input 2: 
//"(a + (a + b))"

//Sample Output 2:

//0


#include<iostream>
using namespace std;
int rebundable(string equation){
    int a = 0;
    int b = 0;
    for(char i : equation){
        
        if(i == '(' || i == ')'){
            b +=1;}
        
       
        else if (i == '*' || i == '+' || i == '-' || i == '/'){
            a++;}
        
    }
    if ((b/2) <= a){
            return 0;}
    return 1;
}
int main(){
    string equation;
    getline(cin,equation);
    cout << rebundable(equation) << endl;
}
