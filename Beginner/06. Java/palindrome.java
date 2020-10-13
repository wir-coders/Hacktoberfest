//Ansh Sharma 
//2nd October 2020
// This program checks if a number is Palindrome or not. A palindrome number is a number which remains the same even if the digits are reversed. Example : 11 is a palindrome number.
import java.util.*;
public class palindrome
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number to be checked");
		int num = sc.nextInt();

		int temp =0 ; // Will store the reversed number
		int original = num; //Stores original number entered
		while (num !=0)
		{
			temp = (temp*10) + (num %10); //The number is reversed last digit by digit
            num = num/10;
		}
		if (temp==original)
		{
			System.out.println("The number entered is palindrome");

		}
		else
		{
			System.out.println("The number is not palindrome");

		}

	}
}