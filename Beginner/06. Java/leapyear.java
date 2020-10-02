//Ansh Sharma
//2nd October 2020
//This program checks if the number entered is a leap year or not.
import java.util.*;
public class leapyear
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner (System.in);
		System.out.println("Enter year to be checked as leap year");
		int year = sc.nextInt();//Stores the inout
		if(year%4==0&&year%100!=0 || year%400==0)//Condition for a leap year
		{
			System.out.println("The year entered is a leap year");
		}
		else
		{
			System.out.println("The year entered is not a leap year");
		}
	}
}