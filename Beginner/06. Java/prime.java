//Ansh Sharma
//2nd October 2020
//This program checks if a number is prime or not. A prime number is a number which is only divisble by 1 and itself
import java.util.*;
public class prime
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner (System.in);
		System.out.println("Enter number to be checked");
		int num = sc.nextInt();//Stores user input
		int factors = 1;//Stores number of factors
		for (int i = 2;i<=(num/2);i++)
		{
			if(num%i==0)
			{
				factors++;//Updates number of Factors
			}
		}
		if(factors==1)
		{
			System.out.println("The number entered is Prime");

		}
		else
		{
			System.out.println("The number entered is not Prime");
		}
	}
}