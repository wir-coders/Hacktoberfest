//this is the calc advance than arithmetic calculator. simple calc can only perform some particular operations like addition,
//subtraction, multiplicatin and division but this calc is made to do some advance calculation like performing trigonometric 
//functions.
//sin(), cos(), and calculus like logarithmic of any two number.

//Here user need to run the code then list of some operatioins will be displayed and user can enter a number of his/her choice. 
//After that he will be asked to enter any two numbers(either integer or float), and he/she will get result as per his/ her 
//requirments.

//This is how code works and user can do any mathematical calculations easily which is done using a standard scientific calculator.

#include<bits/stdc++.h>
using namespace std;
int main()
{
	std::cout<<"    "<<"-------"<<" "<<"-------"<<" "<<"-     -"<<" "<<"-------"<<" "<<"-    -"<<" "<<"-------"<<" "<<"-------"<<"     "<<"-------"<<" "<<"-------"<<" "<<"-     "<<" "<<"-------"<<"\n";
	std::cout<<"    "<<"'     '"<<" "<<" '    '"<<" "<<"'     '"<<" "<<"'     '"<<" "<<"' '  '"<<" "<<"'      "<<" "<<"'      "<<"     "<<"'      "<<" "<<"'     '"<<" "<<"'     "<<" "<<"'      "<<"\n";
	std::cout<<"    "<<"'-----'"<<" "<<" '    '"<<" "<<"'     '"<<" "<<"'-----'"<<" "<<"'   ''"<<" "<<"'      "<<" "<<"-------"<<"     "<<"'      "<<" "<<"'-----'"<<" "<<"'     "<<" "<<"'      "<<"\n";
	std::cout<<"    "<<"'     '"<<" "<<" '    '"<<" "<<"'     '"<<" "<<"'     '"<<" "<<"'    '"<<" "<<"'      "<<" "<<"'      "<<"     "<<"'      "<<" "<<"'     '"<<" "<<"'     "<<" "<<"'      "<<"\n";
	std::cout<<"    "<<"'     '"<<" "<<"------'"<<" "<<" '---' "<<" "<<"'     '"<<" "<<"'    '"<<" "<<"-------"<<" "<<"'------"<<"     "<<"-------"<<" "<<"'     '"<<" "<<"'-----"<<" "<<"-------"<<"\n";
    float a,b,res;
    int v;
//    loop to perform various operations.
    while(true){
    std::cout<<"\t\t 1. Addition of a and b\n";
    std::cout<<"\t\t 2. Subtraction of a and b\n";
    std::cout<<"\t\t 3. multiplication of a and b\n";
    std::cout<<"\t\t 4. division of a and b\n";
	std::cout<<"\t\t 5. square of a and b\n";    
	std::cout<<"\t\t 6. square root of a and b\n";
    std::cout<<"\t\t 7. a to the power b\n";
    std::cout<<"\t\t 8. sin of a and b\n";
    std::cout<<"\t\t 9. cos of a and b\n";
    std::cout<<"\t\t 10. tan of a and b\n";
    std::cout<<"\t\t 11. exponent of a and b\n";
    std::cout<<"\t\t 12. log of a and b\n";
    std::cout<<"\t\t 13. inverse of a and b\n";
    std::cout<<"\t\t 14. ln of a and b\n";
    std::cout<<"\t\t 15. Exit\n\n";
//    user need to enter any number from 1 to 15 
    std::cout<<"which operation do you wants to perform?\n";
    std::cin>>v;
	
    if(v==15){
    	break;
	}
//    to get input from user for any two numbers.
    std::cout<<"Enter any two numbers a and b: ";
    std::cin>>a>>b;
//	switch statement is used to get different results based on users input.
    switch(v){
        case 1: 
            std::cout<<"summation is : "<<(a+b)<<"\n";
            break;

        case 2: 
            std::cout<<"subtraction is : "<<(a-b)<<"\n";
            break;

        case 3: 
            std::cout<<"multiplication is : "<<(a*b)<<"\n";
			break;
        case 4: 
        	res = a/b;
            std::cout<<"division is : "<<(res)<<"\n";
			break;
			
		case 5: 
            std::cout<<"square of a :"<<(a*a) <<"\nsquare of b : "<<(b*b)<<"\n";
			break;
			
		case 6: 
            std::cout<<"square root of a is : "<<(sqrt(a))<<"\nsquare root of b is : "<<(sqrt(b))<<"\n";
			break;
			
		case 7: 
            std::cout<<"a to the power of b is : "<<pow(a,b)<<"\n";
			break;
			
		case 8: 
            std::cout<<"sin of a is: "<<sin(a)<<"\n"<<"sin of b is: "<<sin(b)<<"\n";
			break;
			    
		case 9: 
            std::cout<<"cos of a is: "<<cos(a)<<"\n"<<"cos of b is: "<<cos(b)<<"\n";
			break;
				
		case 10: 
            std::cout<<"tan of a is: "<<tan(a)<<"\n"<<"tan of b is: "<<tan(b)<<"\n";
			break;
		
		case 11: 
            std::cout<<"exponent of a is: "<<exp(a)<<"\n"<<"exponent of b is: "<<exp(b)<<"\n";
			break;
			
		case 12: 
            std::cout<<"log of a is: "<<(log(a)/2.303)<<"\n"<<"log of b is: "<<(log(b)/2.303)<<"\n";
			break;
			
		case 13: 
            std::cout<<"inverse of a is: "<<(1/a)<<"\n"<<"inverse of b is: "<<(1/b)<<"\n";
			break;
			
		case 14: 
            std::cout<<"ln of a is: "<<(log(a))<<"\n"<<"ln of b is: "<<(log(b))<<"\n";
			break;
//		default is used when user enter wrong input or invalid number(not present in the list of choices.) 							
        default:
            std::cout<<"invalid input!\n";
            break;
    }
}
}

