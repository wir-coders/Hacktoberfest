import java.util.*;

public class SieveOfEratosthenes {
    void sieve(int n) {
        boolean primeArray[] = new boolean[n + 1];
        for (int i = 0; i < n + 1; i++) {
            primeArray[i] = true;
        }

        for (int p = 2; p * p <= n; p++) {
            if (primeArray[p] == true) {
                for (int i = p * p; i <= n; i += p)
                    primeArray[i] = false;
            }
        }

        String output = "";

        for (int i = 2; i <= n; i++) {
            if (primeArray[i] == true)
                output = output + i + " ";
        }

        System.out.println((output.trim()).replace(" ", ", "));
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of 'n' - ");
        int n = sc.nextInt();
        System.out.println("Prime Numbers Less than or Equal to " + n + " are - ");
        SieveOfEratosthenes obj = new SieveOfEratosthenes();
        obj.sieve(n);
        sc.close();
    }
}
