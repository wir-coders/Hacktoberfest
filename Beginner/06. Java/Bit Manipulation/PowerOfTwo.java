/* This is a way of checking if a digit is Power of Two or not(for ex. 2,4,8,16 are power of two),
* here we are using the Fact that If the integer is Power of two, It'll have only one set bit.
* */
import java.util.*;
public class PowerOfTwo {
    static boolean PowerOfTwo(int n){
        if (n<=0)
            return false;
        return ((n&(n-1))==0); //unset the right most set bit
    }
    // Driver function
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number to be checked if it is a Power Of two or Not");
        int n =scan.nextInt();
        System.out.println(PowerOfTwo(n));
    }
}
