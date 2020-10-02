/*This is simple method to calcute factorial of given number
 with recursive approach*/
import java.util.Scanner;
class FactorialExUsingRecursion{  
 static int factorial(int n){    
  if (n == 0)    
    return 1;    
  else    
    return(n * factorial(n-1));    
 }    
 public static void main(String args[]){  
  	int i,fact=1; 
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter number to calculate factorial ");
	int number = sc.nextInt();  
  	fact = factorial(number);   
  	System.out.println("Factorial of "+number+" is: "+fact);    
 }  
}  