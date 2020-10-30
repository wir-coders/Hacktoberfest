import java.util.Scanner;

public class toy_shop {

    String[] SoftToys = {"Giant-Teddy-Bear", "Giraffe", "Cat", "Mega-Bear", "Dog", "Lion", "Billy-Bear", "Besty-Bear", "Monkey"};

    /**
     * @param args the command line arguments
     */
    public void display() {
        for (int i = 0; i < SoftToys.length; i++) {
            System.out.println(SoftToys[i]);
        }
    }

    void take() {
        int index = 0;
        Scanner sc = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter Toy Name");

        String name = sc.nextLine();  // Read user input
        for (int i = 0; i < SoftToys.length; i++) {

            if (SoftToys[i].equals(name)) {
                System.out.println("Toy Found" + name);
                index = i;
                break;
            }

        }
        for (int j = index; j < SoftToys.length - 1; j++) {
            SoftToys[j] = SoftToys[j + 1];
            SoftToys[j + 1] = "Empty";

        }
    }

    public static void main(String[] args) {
        Demo d = new Demo();
        d.display();
        d.take();
        d.display();
    }

}
