import java.util.Scanner;
/* Bit toggling/ Setting bit ON or OFF is a way of changing a digit's Binary from 0
to 1 or vice-versa.
* */
public class SetBitOff{
    public static void main(String[] args) { ;
        Scanner sc = new Scanner(System.in);
        //Take input from the user for toggling the Bit
        System.out.println("Enter the no to be turned off");
        int num = sc.nextInt();
        //Take input of the position of the Bit to be turned off from the user
        System.out.println("Enter the position to be off");
        int pos = sc.nextInt();
        int mask = 1 << pos;
        mask = ~mask;
        System.out.println("Digit before turnign off " + Integer.toBinaryString(num));
        num = num & mask;
        System.out.println(Integer.toBinaryString(num));
    }
}
