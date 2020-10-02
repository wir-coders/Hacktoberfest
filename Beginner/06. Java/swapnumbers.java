//Ansh Sharma
//2nd October 2020
//This program swaps two numbers inputted by user using three variables and without using three variables
import java.util.*;
public class swapnumbers
{
	public static void main(String args[])
	{

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a ");
		int a = sc.nextInt();
		System.out.println("Enter b");
		int b = sc.nextInt();
		System.out.println("a = " + a +"\n b= " + b);//Before swap
		//Using three variables
		int temp = b;
		b = a ;
		a = temp;
		System.out.println("Using three vaiables \n "+"a = " + a +"\n b= " + b);//After swap
		//Using only two variables
		System.out.println("Enter a ");
	    a = sc.nextInt();
		System.out.println("Enter b");
		b = sc.nextInt();
		System.out.println("a = " + a +"\n b= " + b);//Before swap
		a = a+b;
		b = a-b;
		a = a-b;
		System.out.println("Using two variables \n "+"a = " + a +"\n b= " + b);//After swap


	}
}